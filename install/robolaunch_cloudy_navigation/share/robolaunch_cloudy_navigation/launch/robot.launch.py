from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(PathJoinSubstitution(
                [FindPackageShare('rplidar_ros'), 'launch', 'rplidar_s1.launch.py']
            )),
            
        ),

        Node(
            package='mecanum_control',
            executable='serial_com',
            name='serial_com',
            )
        ,
    ])
