cmake_minimum_required(VERSION 3.5)
project(robolaunch_cloudy_navigation)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# To use slamware SDK uncomment the following lines and set the correct path to the SDK

# set(SLTC_SDK_DIR "/slamware/slamware_sdk_linux-x86_64-gcc9/linux-x86_64-release")
# set(SLTC_SDK_INC_DIR "/slamware/slamware_sdk_linux-x86_64-gcc9/linux-x86_64-release/include")
# set(SLTC_SDK_LIB_DIR "/slamware/slamware_sdk_linux-x86_64-gcc9/linux-x86_64-release/lib")
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC -std=gnu++11")


find_package(ament_cmake REQUIRED)
find_package(Threads REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)




ament_python_install_package(${PROJECT_NAME})


install(PROGRAMS
  robolaunch_cloudy_navigation/scripts/dynamic_tf_broadcaster.py
  robolaunch_cloudy_navigation/scripts/way_points.py
  robolaunch_cloudy_navigation/scripts/way_points_web.py
  robolaunch_cloudy_navigation/scripts/waypoints_commander.py
  robolaunch_cloudy_navigation/scripts/barcode_reader.py


  DESTINATION lib/${PROJECT_NAME}
)




install(
  DIRECTORY launch rviz config map 
  DESTINATION share/${PROJECT_NAME}
)

install(PROGRAMS 
  sim_launch/sim_launch_all.launch.py
  sim_launch/sim_nav.launch.py
  sim_launch/sim_slam.launch.py

  distributed_launch/cloud.launch.py
  distributed_launch/galactic_container.launch.py
  distributed_launch/robot.launch.py

  DESTINATION share/${PROJECT_NAME}/launch
)

ament_package()
