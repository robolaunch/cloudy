cmake_minimum_required(VERSION 3.5)
project(robolaunch_diffbot_description)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY config ros2_control urdf sensors
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
