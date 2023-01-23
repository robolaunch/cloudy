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

    filter_config_path = PathJoinSubstitution(
        [FindPackageShare('robolaunch_cloudy_navigation'), 'config', 'range_filter.yaml']
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
            PythonLaunchDescriptionSource(slam_launch_path),
            launch_arguments={
                'use_sim_time': LaunchConfiguration("sim"),
                slam_param_name: slam_config_path
            }.items()
        ),

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
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_path],
            condition=IfCondition(LaunchConfiguration("rviz")),
            parameters=[{'use_sim_time': LaunchConfiguration("sim")}]
        )
    ])
