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
        [FindPackageShare('slam_toolbox'), 'launch', 'online_async_launch.py']
    )

    slam_config_path = PathJoinSubstitution(
        [FindPackageShare('robolaunch_cloudy_navigation'), 'config', 'slam.yaml']
    )

    rf2o_launch_path = PathJoinSubstitution(
        [FindPackageShare('rf2o_laser_odometry'), 'launch', 'rf2o_laser_odometry.launch.py']
    )

    diffbot_system_launch_path = PathJoinSubstitution(
        [FindPackageShare('robolaunch_cloudy_bringup'), 'launch', 'diffbot_system.launch.py']
    )

    rviz_config_path = PathJoinSubstitution(
        [FindPackageShare('robolaunch_cloudy_navigation'), 'rviz', 'slam.rviz']
    )

    ekf_config_path = PathJoinSubstitution(
        [FindPackageShare("robolaunch_cloudy_navigation"), "config", "ekf.yaml"]
    )

    range_filter_config_path = PathJoinSubstitution(
        [FindPackageShare('robolaunch_cloudy_navigation'), 'config', 'range_filter.yaml']
    )

    box_filter_config_path = PathJoinSubstitution(
        [FindPackageShare('robolaunch_cloudy_navigation'), 'config', 'box_filter.yaml']
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

        IncludeLaunchDescription(PythonLaunchDescriptionSource(diffbot_system_launch_path)),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(slam_launch_path),
            launch_arguments={
                'use_sim_time': LaunchConfiguration("sim"),
                slam_param_name: slam_config_path
            }.items()
        ), 

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(rf2o_launch_path),
        ),

        # Node(
        #     package='robot_localization',
        #     executable='ekf_node',
        #     name='ekf_filter_node',
        #     output='screen',
        #     parameters=[
        #         ekf_config_path
        #     ],
        #     remappings=[("odometry/filtered", "odom")]
        # ),

        # Node(
        #     package="laser_filters",
        #     executable="scan_to_scan_filter_chain",
        #     parameters=[box_filter_config_path],
        #     # condition=IfCondition(
        #     #     PythonExpression(
        #     #         [LaunchConfiguration("vehicle"), " == 'cloudy_v2'"]
        #     #     )
        #     # ),
        #     remappings=[("scan_filtered", "scan")]
        # ),

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
    






       
