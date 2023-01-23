from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

from launch_ros.actions import Node

world_path = PathJoinSubstitution(
        [FindPackageShare("robolaunch_cloudy_simulator"), "worlds", "playground.world"]
    )

gazebo_path = PathJoinSubstitution(
        [FindPackageShare("gazebo_ros"), "launch", "gazebo.launch.py"]
    )

description_launch_path = PathJoinSubstitution(
        [FindPackageShare("robolaunch_cloudy_description"), "launch", "description.launch.py"]
    )


def generate_launch_description():

    return LaunchDescription([

        IncludeLaunchDescription(
                PythonLaunchDescriptionSource(description_launch_path), 
                launch_arguments={'use_sim_time': 'true'}.items()
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