/*
 * Copyright (C) 2014 SLAMTEC Co., Ltd.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 */


/**
* SLAMWARE Map Dump Utility 
* The current built map will be saved with BMP format
*  
* By CSK
* Copyright (c) 2014 Shanghai SlamTec Co., Ltd.
*/

// runtime support
#include <cstdio>
#include <cstring>
#include <string>
#include <time.h>

// SLAMWARE necessary headers
#include <rpos/rpos.h>
#include <rpos/robot_platforms/slamware_core_platform.h>
#include <rpos/features/location_provider/map.h>
#include "rclcpp/rclcpp.hpp"

#include "geometry_msgs/msg/pose.hpp"
#include "sensor_msgs/msg/laser_scan.hpp"

// C++ Bitmap Library from http://www.partow.net/
#include "bitmap_image.hpp"

using namespace std;
using namespace rpos::robot_platforms;
using namespace rpos::features;
using namespace rpos::features::location_provider;
using namespace rpos::system::detail;
using namespace rpos::system::types;

#define DEFAULT_DUMPIMAGE_FILENAME "slamware_mapdump"
#define DEFAULT_SDP_PORT           1445

SlamwareCorePlatform sdp;


using namespace std::chrono_literals;

/* This example creates a subclass of Node and uses std::bind() to register a
* member function as a callback from the timer. */

class LaserScanPublisher : public rclcpp::Node
{
  public:
    LaserScanPublisher(SlamwareCorePlatform pltfm)
    : Node("laserscan_pub")
    {
      printf("LaserScanPublisher\n");
      
      pose_publisher_ = this->create_publisher<geometry_msgs::msg::Pose>("lidar_position", 10);
      laser_scan_publisher_ = this->create_publisher<sensor_msgs::msg::LaserScan>("scan", 10);

      rclcpp::Clock my_clock(RCL_ROS_TIME);
      rclcpp::Time startScanTime = my_clock.now();
      this->pltfm = pltfm;

      this->tLs = pltfm.getLaserScan();

      rclcpp::Time endScanTime = my_clock.now();
      this->dblScanDur = (endScanTime - startScanTime).seconds();


      timer_ = this->create_wall_timer(
      500ms, std::bind(&LaserScanPublisher::timer_callback, this));

      printf("Node is created\n");


    }

  // euler to quaternion conversion function
    void euler2quaternion(float roll, float pitch, float yaw, float &qx, float &qy, float &qz, float &qw)
    {
        float cy = cos(yaw * 0.5);
        float sy = sin(yaw * 0.5);
        float cr = cos(roll * 0.5);
        float sr = sin(roll * 0.5);
        float cp = cos(pitch * 0.5);
        float sp = sin(pitch * 0.5);
    
        qx = sr * cp * cy - cr * sp * sy;
        qy = cr * sp * cy + sr * cp * sy;
        qz = cr * cp * sy - sr * sp * cy;
        qw = cr * cp * cy + sr * sp * sy;
    }

    

  private:

    void timer_callback()
    {

    //   position ======================================

      
      

      float roll = this->pltfm.getPose().roll();
      float yaw = this->pltfm.getPose().yaw();
      float pitch = this->pltfm.getPose().pitch();
      float x = this->pltfm.getPose().x();
      float y = this->pltfm.getPose().y();
      float z = this->pltfm.getPose().z();
      float qx{0}, qy, qz, qw;

      euler2quaternion(roll, pitch, yaw, qx, qy, qz, qw);

      this->pose.position.x = x;
      this->pose.position.y = y;
      this->pose.position.z = z;
      this->pose.orientation.x = qx;
      this->pose.orientation.y = qy;
      this->pose.orientation.z = qz;
      this->pose.orientation.w = qw;

      
    //   RCLCPP_INFO(this->get_logger(), "Lidar x: '%.2f'", pose.position.x);
      pose_publisher_->publish(this->pose);

    //   laser scan ====================================

      this->tLs = this->pltfm.getLaserScan();
      const auto& points = tLs.getLaserPoints();


      rclcpp::Clock my_clock(RCL_ROS_TIME);
      this->scan.header.stamp = my_clock.now();

      this->scan.header.frame_id = "laser";
      fillRangeMinMaxInMsg_(points, this->scan);

      this->scan.ranges.resize(points.size());

            for (size_t i = 0; i < points.size(); ++i)
            {
                if (!points[i].valid())
                {
                    this->scan.ranges[i] = std::numeric_limits<float>::infinity();
                }
                else
                {
                    this->scan.ranges[i] = points[i].distance();
                }
            }

            this->scan.angle_min =  points.front().angle();
            this->scan.angle_max =  points.back().angle();
            this->scan.angle_increment = (this->scan.angle_max - this->scan.angle_min) / (double)(this->scan.ranges.size() - 1);
            this->scan.scan_time = dblScanDur;
            this->scan.time_increment = dblScanDur / (double)(this->scan.ranges.size() - 1);

            this->laser_scan_publisher_->publish(this->scan);
    }

    void fillRangeMinMaxInMsg_(const std::vector<rpos::core::LaserPoint> & laserPoints
            , sensor_msgs::msg::LaserScan& msgScan
            ) const
    {
        msgScan.range_min = std::numeric_limits<float>::infinity();
        msgScan.range_max = 0.0f;
        for (auto cit = laserPoints.cbegin(), citEnd = laserPoints.cend(); citEnd != cit; ++cit)
        {
            if (cit->valid())
            {
                const float tmpDist = cit->distance();
                
                if (tmpDist < msgScan.range_min)
                {
                    msgScan.range_min = std::max<float>(0.0f, tmpDist);
                }

                if (msgScan.range_max < tmpDist)
                {
                    msgScan.range_max = tmpDist;
                }
            }
        }
    }

    rclcpp::TimerBase::SharedPtr timer_;
    rclcpp::Publisher<geometry_msgs::msg::Pose>::SharedPtr pose_publisher_;
    rclcpp::Publisher<sensor_msgs::msg::LaserScan>::SharedPtr laser_scan_publisher_;
    size_t count_;
    SlamwareCorePlatform pltfm;
    sensor_msgs::msg::LaserScan scan;
    double dblScanDur;
    rpos::features::system_resource::LaserScan tLs;
    geometry_msgs::msg::Pose pose = geometry_msgs::msg::Pose();

};

void showHelp(int argc, const char * argv[])
{
    printf("SLAMWARE Map Dump Utility\n\n"
           "USAGE:\n"
           "%s [OPTS] [-o filename] <SDP IP Address>\n"
           "SDP IP Address      The ip address string of the SLAMWARE SDP.\n"
           "-o  filename        Bitmap filename to be used to save the dumped map.\n"
           "                    If not specified, the default name %s will be used.\n"
           "-p  port            SDP Server port.\n"
           "                    No file will be generated.\n"
           "                    By default, the port %d will be used.\n"
           "--txt-format        The dumped file will be saved in Text format instead of BMP.\n"
           "--info-only         Only display map size and related info. \n"
           , argv[0], DEFAULT_DUMPIMAGE_FILENAME, DEFAULT_SDP_PORT);
}


bool saveToBmp(const char * filename, Map map)
{
    std::string finalFilename = filename;
    printf(finalFilename.c_str());
    finalFilename += ".bmp";

    bitmap_image mapBitmap(map.getMapDimension().x(), map.getMapDimension().y());

    for (int posY = 0; posY < map.getMapDimension().y(); ++posY)
    {
        for (int posX = 0; posX < map.getMapDimension().x(); ++posX)
        {
            rpos::system::types::_u8 cellValue = ((rpos::system::types::_u8)128U) + map.getMapData()[posX + (map.getMapDimension().y()-posY-1) * map.getMapDimension().x()];
            mapBitmap.set_pixel(posX, posY, cellValue, cellValue, cellValue);
        }
    }
    mapBitmap.save_image(finalFilename);
    return true;
}

bool saveToTxt(const char * filename, Map map)
{
    std::string finalFilename = filename;
    finalFilename += ".txt";

    FILE * fp = fopen(finalFilename.c_str(), "w");
    if (!fp) {
        fprintf(stderr, "Cannot create the file %s.\n", finalFilename.c_str());
        return false;
    }

    fprintf(fp, "# SLAMWARE MAP FILE\n");
    fprintf(fp, "Area: %.4f, %.4f, %.4f, %.4f\n", map.getMapArea().x(), map.getMapArea().y(), map.getMapArea().width(), map.getMapArea().height());
    fprintf(fp, "Cell Resolution: %.4f, %.4f\n", map.getMapResolution().x(), map.getMapResolution().y());
    fprintf(fp, "Cell Dimension: %u, %u\n", map.getMapDimension().x(), map.getMapDimension().y());


    for (int posY = 0; posY < map.getMapDimension().y(); ++posY)
    {
        for (int posX = 0; posX < map.getMapDimension().x(); ++posX)
        {
            fprintf(fp, "%d, ",  (char)map.getMapData()[posX + posY *map.getMapDimension().x() ]);

        }
        fprintf(fp, "\n");
    }

    fclose(fp);

    return true;
}

void displayMapInfo(Map map)
{
    printf("> Map Area: (%.4f,%.4f,%.4f,%.4f)\n"
        , map.getMapArea().left()
        , map.getMapArea().top()
        , map.getMapArea().right()
        , map.getMapArea().bottom());

    printf("> Cell Dimension: (%u,%u)\n"
        , map.getMapDimension().x()
        , map.getMapDimension().y());

    printf("> Cell Resolution: (%.4f,%.4f)\n"
        , map.getMapResolution().x()
        , map.getMapResolution().y());
#ifdef _WIN32
    printf("> Timestamp: %I64u\n"
        , map.getMapTimestamp());
#else
    printf("> Timestamp: %llu\n"
        , map.getMapTimestamp());
#endif
}

void displayLocalizationInfo(const rpos::core::Pose & pose)
{
    printf("> Position: (%.4f,%.4f,%.4f)\n"
        , pose.x(), pose.y(), pose.z());

    printf("> Heading: %.4f\n"
        , pose.yaw()*180.0f/M_PI);
}


int main(int argc, const char * argv[])
{
    bool         opt_needShowHelp = false;
    bool         opt_noSave       = false;
    bool         opt_txtFileMode  = false;
    const char * opt_sdpIPAddress = NULL;
    const char * opt_dumpImageFilename = DEFAULT_DUMPIMAGE_FILENAME;
    int          opt_sdpPort = DEFAULT_SDP_PORT;

    // parse the command line...
    for (int currentArg = 1;  currentArg< argc; ++currentArg) 
    {
        if (strcmp(argv[currentArg], "-o") == 0) {
            if (++currentArg < argc) {
                opt_dumpImageFilename = argv[currentArg];
            }
        } else if (strcmp(argv[currentArg], "-h") == 0) {
            opt_needShowHelp = true;
        } else if (strcmp(argv[currentArg], "--txt-format") == 0) {
            opt_txtFileMode = true;
        } else if (strcmp(argv[currentArg], "--info-only") == 0) {
            opt_noSave = true;
        } else if (strcmp(argv[currentArg], "-p") == 0) {
            if (++currentArg < argc) {
                opt_sdpPort = atoi(argv[currentArg]);
            } else {
                opt_needShowHelp = true;
            }
        }else {
            opt_sdpIPAddress = argv[currentArg];
        }
    }
    printf("Connecting to the SDP @ %s...\n", opt_sdpIPAddress);



    if (opt_needShowHelp || !opt_sdpIPAddress) {
        showHelp(argc, argv);
        return -1;
    }

    
    
    try {
        sdp = SlamwareCorePlatform::connect(opt_sdpIPAddress, opt_sdpPort);

        printf("Fetching Map Info...\n");
        rpos::core::RectangleF knownArea = sdp.getKnownArea(MapTypeBitmap8Bit, rpos::features::location_provider::EXPLORERMAP);
        Map map = sdp.getMap(MapTypeBitmap8Bit, knownArea, rpos::features::location_provider::EXPLORERMAP);
        displayMapInfo(map);

        printf("Fetching Localization Info...\n");
        rpos::core::Pose robotPose = sdp.getPose();
        displayLocalizationInfo(robotPose);

        if (opt_noSave) {
            return 0;
        }

        // dump the map data to file....

        if (opt_txtFileMode) {
            if (!saveToTxt(opt_dumpImageFilename, map)) {
                return -3;
            }
        } else {
            if (!saveToBmp(opt_dumpImageFilename, map)) {
                
                return -3;
            }else {
                printf("Map saved to %s.bmp.\n", opt_dumpImageFilename);
            }

        }
        rclcpp::init(0, nullptr);
        printf("rcllcpp initialized.\n");

        rclcpp::spin(std::make_shared<LaserScanPublisher>(sdp));

        
        rclcpp::shutdown();
        printf("Node is shutdown\n");



        return 0;
    } catch (ExceptionBase & e) {
        fprintf(stderr, "Failed: %s\n", e.what());
        return -2;
    }



    
}
