from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from launch_ros.substitutions import FindPackageShare

from launch_ros.actions import Node

world_path = PathJoinSubstitution(
        [FindPackageShare("robolaunch_cloudy_simulator"), "worlds", "industrial-warehouse.sdf"]
    )

gazebo_path = PathJoinSubstitution(
        [FindPackageShare("gazebo_ros"), "launch", "gazebo.launch.py"]
    )

description_launch_path = PathJoinSubstitution(
        [FindPackageShare("robolaunch_cloudy_description"), "launch", "description.launch.py"]
    )


def generate_launch_description():

    return LaunchDescription([

        DeclareLaunchArgument(
            name="vehicle",
            default_value="'cloudy_v2'",
            description="vehicle type"
        ),

        IncludeLaunchDescription(
                PythonLaunchDescriptionSource(description_launch_path), 
                launch_arguments={
                    'use_sim_time': 'true',
                    'vehicle': LaunchConfiguration("vehicle")
                }.items()
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gazebo_path),
            launch_arguments={
                'use_sim_time': str("true"),
                'world': world_path,
            }.items()
        ),
         
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-topic', 'robot_description', '-entity', 'my_bot'],
            output='screen')
    ])