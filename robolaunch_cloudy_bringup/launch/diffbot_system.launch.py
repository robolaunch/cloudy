import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():

    arg_show_rviz = DeclareLaunchArgument(
        "start_rviz",
        default_value="true",
        description="start RViz automatically with the launch file",
    )

    # Get URDF via xacro
    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            PathJoinSubstitution(
                [FindPackageShare("robolaunch_cloudy_description"), "urdf", "diffbot_system.urdf.xacro"]
            ),
        ]
    )
    robot_description = {"robot_description": robot_description_content}

    diffbot_diff_drive_controller = PathJoinSubstitution(
        [
            FindPackageShare("robolaunch_cloudy_bringup"),
            "config",
            "diffbot_diff_drive_controller.yaml",
        ]
    )

    node_robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[robot_description],
        remappings=[
            ("diff_drive_controller/cmd_vel_unstamped", "cmd_vel"),
        ],
        
    )

    controller_manager_node = Node(
        package="controller_manager",
        executable="ros2_control_node",
        parameters=[robot_description, diffbot_diff_drive_controller],
        remappings=[
            ("diff_drive_controller/cmd_vel_unstamped", "cmd_vel"),
        ],
        output={
            "stdout": "screen",
            "stderr": "screen",
        },
        
        
    )

    spawn_dd_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["diffbot_base_controller"],
        output="screen",
        remappings=[
            ("diff_drive_controller/cmd_vel_unstamped", "cmd_vel"),
        ],
    )
    spawn_jsb_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster"],
        output="screen",
        remappings=[
            ("diff_drive_controller/cmd_vel_unstamped", "cmd_vel"),
        ],
    )

    rviz_config_file = PathJoinSubstitution(
        [FindPackageShare("robolaunch_cloudy_description"), "config", "diffbot.rviz"]
    )
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        arguments=["-d", rviz_config_file],
        condition=IfCondition(LaunchConfiguration("start_rviz")),
    )


    return LaunchDescription(
        [
            arg_show_rviz,
            node_robot_state_publisher,
            controller_manager_node,
            spawn_dd_controller,
            spawn_jsb_controller,
            rviz_node,
        ]
    )
