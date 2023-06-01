import os
from launch import LaunchDescription
from launch import LaunchContext
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition
from launch.substitutions import EnvironmentVariable
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

def generate_launch_description():

    slam_launch_path = PathJoinSubstitution(
        [FindPackageShare('robolaunch_cloudy_navigation'), 'launch', 'cloudy_slam.launch.py']
    )
    nav_launch_path = PathJoinSubstitution(
        [FindPackageShare('robolaunch_cloudy_navigation'), 'launch', 'cloudy_nav.launch.py']
    )

    waypoints_path = PathJoinSubstitution(
        [FindPackageShare('robolaunch_cloudy_navigation'), 'robolaunch_cloudy_navigation', 'scripts', 'way_points.py']
    )
    
         
    return LaunchDescription([
        
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(slam_launch_path),
            
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(nav_launch_path),
            launch_arguments={
                'rviz': 'true',
                
            }.items()
        ),

        # Node(
        #     package='robolaunch_cloudy_navigation',
        #     executable='way_points.py',
        #     name='way_points',
        #     output='screen',
        # ),

        # Node(
        #      package='rviz2',
        #      executable='rviz2',
        #      name='rviz2',
        #      output='screen',
        #      arguments=['-d', rviz_config_path],
        # )

        
    ])