# Install script for directory: /home/mert/gokhan_cloudy/src/robolaunch_cloudy_navigation

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/mert/gokhan_cloudy/src/install/robolaunch_cloudy_navigation")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robolaunch_cloudy_navigation/environment" TYPE FILE FILES "/home/mert/gokhan_cloudy/src/build/robolaunch_cloudy_navigation/ament_cmake_environment_hooks/pythonpath.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robolaunch_cloudy_navigation/environment" TYPE FILE FILES "/home/mert/gokhan_cloudy/src/build/robolaunch_cloudy_navigation/ament_cmake_environment_hooks/pythonpath.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/local/lib/python3.10/dist-packages/robolaunch_cloudy_navigation-0.0.0-py3.10.egg-info" TYPE DIRECTORY FILES "/home/mert/gokhan_cloudy/src/build/robolaunch_cloudy_navigation/ament_cmake_python/robolaunch_cloudy_navigation/robolaunch_cloudy_navigation.egg-info/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/local/lib/python3.10/dist-packages/robolaunch_cloudy_navigation" TYPE DIRECTORY FILES "/home/mert/gokhan_cloudy/src/robolaunch_cloudy_navigation/robolaunch_cloudy_navigation/" REGEX "/[^/]*\\.pyc$" EXCLUDE REGEX "/\\_\\_pycache\\_\\_$" EXCLUDE)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(
        COMMAND
        "/usr/bin/python3.10" "-m" "compileall"
        "/home/mert/gokhan_cloudy/src/install/robolaunch_cloudy_navigation/local/lib/python3.10/dist-packages/robolaunch_cloudy_navigation"
      )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/robolaunch_cloudy_navigation" TYPE PROGRAM FILES
    "/home/mert/gokhan_cloudy/src/robolaunch_cloudy_navigation/robolaunch_cloudy_navigation/scripts/dynamic_tf_broadcaster.py"
    "/home/mert/gokhan_cloudy/src/robolaunch_cloudy_navigation/robolaunch_cloudy_navigation/scripts/way_points.py"
    "/home/mert/gokhan_cloudy/src/robolaunch_cloudy_navigation/robolaunch_cloudy_navigation/scripts/way_points_web.py"
    "/home/mert/gokhan_cloudy/src/robolaunch_cloudy_navigation/robolaunch_cloudy_navigation/scripts/waypoints_commander.py"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robolaunch_cloudy_navigation" TYPE DIRECTORY FILES
    "/home/mert/gokhan_cloudy/src/robolaunch_cloudy_navigation/launch"
    "/home/mert/gokhan_cloudy/src/robolaunch_cloudy_navigation/rviz"
    "/home/mert/gokhan_cloudy/src/robolaunch_cloudy_navigation/config"
    "/home/mert/gokhan_cloudy/src/robolaunch_cloudy_navigation/map"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robolaunch_cloudy_navigation/launch" TYPE PROGRAM FILES
    "/home/mert/gokhan_cloudy/src/robolaunch_cloudy_navigation/sim_launch/sim_launch_all.launch.py"
    "/home/mert/gokhan_cloudy/src/robolaunch_cloudy_navigation/sim_launch/sim_nav.launch.py"
    "/home/mert/gokhan_cloudy/src/robolaunch_cloudy_navigation/sim_launch/sim_slam.launch.py"
    "/home/mert/gokhan_cloudy/src/robolaunch_cloudy_navigation/distributed_launch/cloud.launch.py"
    "/home/mert/gokhan_cloudy/src/robolaunch_cloudy_navigation/distributed_launch/galactic_container.launch.py"
    "/home/mert/gokhan_cloudy/src/robolaunch_cloudy_navigation/distributed_launch/robot.launch.py"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/package_run_dependencies" TYPE FILE FILES "/home/mert/gokhan_cloudy/src/build/robolaunch_cloudy_navigation/ament_cmake_index/share/ament_index/resource_index/package_run_dependencies/robolaunch_cloudy_navigation")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/parent_prefix_path" TYPE FILE FILES "/home/mert/gokhan_cloudy/src/build/robolaunch_cloudy_navigation/ament_cmake_index/share/ament_index/resource_index/parent_prefix_path/robolaunch_cloudy_navigation")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robolaunch_cloudy_navigation/environment" TYPE FILE FILES "/opt/ros/humble/share/ament_cmake_core/cmake/environment_hooks/environment/ament_prefix_path.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robolaunch_cloudy_navigation/environment" TYPE FILE FILES "/home/mert/gokhan_cloudy/src/build/robolaunch_cloudy_navigation/ament_cmake_environment_hooks/ament_prefix_path.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robolaunch_cloudy_navigation/environment" TYPE FILE FILES "/opt/ros/humble/share/ament_cmake_core/cmake/environment_hooks/environment/path.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robolaunch_cloudy_navigation/environment" TYPE FILE FILES "/home/mert/gokhan_cloudy/src/build/robolaunch_cloudy_navigation/ament_cmake_environment_hooks/path.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robolaunch_cloudy_navigation" TYPE FILE FILES "/home/mert/gokhan_cloudy/src/build/robolaunch_cloudy_navigation/ament_cmake_environment_hooks/local_setup.bash")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robolaunch_cloudy_navigation" TYPE FILE FILES "/home/mert/gokhan_cloudy/src/build/robolaunch_cloudy_navigation/ament_cmake_environment_hooks/local_setup.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robolaunch_cloudy_navigation" TYPE FILE FILES "/home/mert/gokhan_cloudy/src/build/robolaunch_cloudy_navigation/ament_cmake_environment_hooks/local_setup.zsh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robolaunch_cloudy_navigation" TYPE FILE FILES "/home/mert/gokhan_cloudy/src/build/robolaunch_cloudy_navigation/ament_cmake_environment_hooks/local_setup.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robolaunch_cloudy_navigation" TYPE FILE FILES "/home/mert/gokhan_cloudy/src/build/robolaunch_cloudy_navigation/ament_cmake_environment_hooks/package.dsv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/ament_index/resource_index/packages" TYPE FILE FILES "/home/mert/gokhan_cloudy/src/build/robolaunch_cloudy_navigation/ament_cmake_index/share/ament_index/resource_index/packages/robolaunch_cloudy_navigation")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robolaunch_cloudy_navigation/cmake" TYPE FILE FILES
    "/home/mert/gokhan_cloudy/src/build/robolaunch_cloudy_navigation/ament_cmake_core/robolaunch_cloudy_navigationConfig.cmake"
    "/home/mert/gokhan_cloudy/src/build/robolaunch_cloudy_navigation/ament_cmake_core/robolaunch_cloudy_navigationConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/robolaunch_cloudy_navigation" TYPE FILE FILES "/home/mert/gokhan_cloudy/src/robolaunch_cloudy_navigation/package.xml")
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/mert/gokhan_cloudy/src/build/robolaunch_cloudy_navigation/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
