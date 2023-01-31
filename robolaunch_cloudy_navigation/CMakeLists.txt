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
find_package(rclcpp_action REQUIRED)
find_package(rclcpp_lifecycle REQUIRED)
find_package(std_msgs REQUIRED)
find_package(visualization_msgs REQUIRED)
find_package(nav2_util REQUIRED)
find_package(nav2_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(nav2_costmap_2d REQUIRED)
find_package(nav2_core REQUIRED)
find_package(pluginlib REQUIRED)

include_directories(
  include
)


set(library_name ${PROJECT_NAME}_plugin)

set(dependencies
  rclcpp
  rclcpp_action
  rclcpp_lifecycle
  std_msgs
  visualization_msgs
  nav2_util
  nav2_msgs
  nav_msgs
  geometry_msgs
  builtin_interfaces
  tf2_ros
  nav2_costmap_2d
  nav2_core
  pluginlib
)

ament_python_install_package(${PROJECT_NAME})

add_library(${library_name} SHARED
  src/straight_line_planner.cpp
)

ament_target_dependencies(${library_name}
  ${dependencies}
)

target_compile_definitions(${library_name} PUBLIC "PLUGINLIB__DISABLE_BOOST_FUNCTIONS")


pluginlib_export_plugin_description_file(nav2_core global_planner_plugin.xml)

install(TARGETS ${library_name}
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY include/
  DESTINATION include/
)

install(FILES global_planner_plugin.xml
  DESTINATION share/${PROJECT_NAME}
)


install(PROGRAMS
  robolaunch_cloudy_navigation/scripts/dynamic_tf_broadcaster.py
  robolaunch_cloudy_navigation/scripts/way_points.py
  robolaunch_cloudy_navigation/scripts/waypoints_commander.py

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

ament_export_include_directories(include)
ament_export_libraries(${library_name})
ament_export_dependencies(${dependencies})
ament_package()
