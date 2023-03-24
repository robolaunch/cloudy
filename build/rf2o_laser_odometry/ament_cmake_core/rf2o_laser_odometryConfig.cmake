# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_rf2o_laser_odometry_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED rf2o_laser_odometry_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(rf2o_laser_odometry_FOUND FALSE)
  elseif(NOT rf2o_laser_odometry_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(rf2o_laser_odometry_FOUND FALSE)
  endif()
  return()
endif()
set(_rf2o_laser_odometry_CONFIG_INCLUDED TRUE)

# output package information
if(NOT rf2o_laser_odometry_FIND_QUIETLY)
  message(STATUS "Found rf2o_laser_odometry: 0.1.0 (${rf2o_laser_odometry_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'rf2o_laser_odometry' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${rf2o_laser_odometry_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(rf2o_laser_odometry_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${rf2o_laser_odometry_DIR}/${_extra}")
endforeach()
