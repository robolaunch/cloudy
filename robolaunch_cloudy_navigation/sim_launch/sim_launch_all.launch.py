import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node


def generate_launch_description():

    nav2_launch_path = PathJoinSubstitution(
        [FindPackageShare('robolaunch_cloudy_navigation'), 'launch', 'sim_nav.launch.py']
    )

    gazebo_launch_path = PathJoinSubstitution(
        [FindPackageShare('robolaunch_cloudy_simulator'), 'launch', 'gazebo.launch.py']
    )

    rviz_config_path = PathJoinSubstitution(
        [FindPackageShare('robolaunch_cloudy_navigation'), 'rviz', 'nav.rviz']
    )

    slam_launch_path = PathJoinSubstitution(
        [FindPackageShare('robolaunch_cloudy_navigation'), 'launch', 'sim_slam.launch.py']
    )

    return LaunchDescription([

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gazebo_launch_path),
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(slam_launch_path),
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(nav2_launch_path),
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_path],
        )
    ])