# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_robolaunch_cloudy_bringup_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED robolaunch_cloudy_bringup_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(robolaunch_cloudy_bringup_FOUND FALSE)
  elseif(NOT robolaunch_cloudy_bringup_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(robolaunch_cloudy_bringup_FOUND FALSE)
  endif()
  return()
endif()
set(_robolaunch_cloudy_bringup_CONFIG_INCLUDED TRUE)

# output package information
if(NOT robolaunch_cloudy_bringup_FIND_QUIETLY)
  message(STATUS "Found robolaunch_cloudy_bringup: 0.0.0 (${robolaunch_cloudy_bringup_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'robolaunch_cloudy_bringup' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${robolaunch_cloudy_bringup_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(robolaunch_cloudy_bringup_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${robolaunch_cloudy_bringup_DIR}/${_extra}")
endforeach()
