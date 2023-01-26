# Copyright (c) 2021 Juan Miguel Jimeno
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import launch_ros
from launch import LaunchDescription
from launch import LaunchContext
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, PythonExpression
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition
from launch.substitutions import EnvironmentVariable
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node


def generate_launch_description():
    slam_launch_path = PathJoinSubstitution(
        [FindPackageShare('slam_toolbox'), 'launch', 'online_async_launch.py']
    )

    filter_launch_path = PathJoinSubstitution(
        [FindPackageShare('laser_filters'), 'examples', 'shadow_filter_example.launch.py']
    )

    slam_config_path = PathJoinSubstitution(
        [FindPackageShare('robolaunch_cloudy_navigation'), 'config', 'sim_slam.yaml']
    )

    rviz_config_path = PathJoinSubstitution(
        [FindPackageShare('robolaunch_cloudy_navigation'), 'rviz', 'slam.rviz']
    )

    ekf_config_path = PathJoinSubstitution(
        [FindPackageShare('robolaunch_cloudy_navigation'), 'config', 'ekf.yaml']
    )

    filter_config_path = PathJoinSubstitution(
        [FindPackageShare('robolaunch_cloudy_navigation'), 'config', 'range_filter.yaml']
    )

    box_filter_config_path = PathJoinSubstitution(
        [FindPackageShare('robolaunch_cloudy_navigation'), 'config', 'box_filter.yaml']
    )

    rf2o_launch_path = PathJoinSubstitution(
        [FindPackageShare('rf2o_laser_odometry'), 'launch', 'rf2o_laser_odometry.launch.py']
    )    
    
    
    lc = LaunchContext()
    ros_distro = EnvironmentVariable('ROS_DISTRO')
    slam_param_name = 'slam_params_file'
    if ros_distro.perform(lc) == 'foxy': 
        slam_param_name = 'params_file'

    return LaunchDescription([
        DeclareLaunchArgument(
            name='sim', 
            default_value='false',
            description='Enable use_sime_time to true'
        ),

        DeclareLaunchArgument(
            name='rviz', 
            default_value='false',
            description='Run rviz'
        ),

        DeclareLaunchArgument(
            name='vehicle', 
            default_value="'cloudy_v2'",
            description='vehicle name'
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(rf2o_launch_path),
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(slam_launch_path),
            launch_arguments={
                'use_sim_time': LaunchConfiguration("sim"),
                slam_param_name: slam_config_path
            }.items()
        ),

        # launch_ros.actions.Node(
        #     package='robot_localization',
        #     executable='ekf_node',
        #     name='ekf_filter_node',
        #     output='screen',
        #     parameters=[ekf_config_path , {'use_sim_time': LaunchConfiguration('sim')}]
        # ),

        Node(
            package="laser_filters",
            executable="scan_to_scan_filter_chain",
            parameters=[filter_config_path],
            condition=IfCondition(
                PythonExpression(
                    [LaunchConfiguration("vehicle"), " == 'cloudy_v2'"]
                )
            ),
        ),

        Node(
            package="laser_filters",
            executable="scan_to_scan_filter_chain",
            parameters=[box_filter_config_path],
            condition=IfCondition(
                PythonExpression(
                    [LaunchConfiguration("vehicle"), " == 'arcelik'"]
                )
            ),
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_path],
            condition=IfCondition(LaunchConfiguration("rviz")),
            parameters=[{'use_sim_time': LaunchConfiguration("sim")}]
        )


    ])
