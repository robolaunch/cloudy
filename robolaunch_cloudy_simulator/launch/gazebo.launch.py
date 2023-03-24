from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration, PythonExpression
from launch.conditions import IfCondition
from launch_ros.substitutions import FindPackageShare

from launch_ros.actions import Node

playground_world_path = PathJoinSubstitution(
        [FindPackageShare("robolaunch_cloudy_simulator"), "worlds", "playground.world"]
    )

counter_world_path = PathJoinSubstitution(
        [FindPackageShare("robolaunch_cloudy_simulator"), "worlds","arcelik_warehouse","env_counter.world"]
    )

warehouse_world_path = PathJoinSubstitution(
        [FindPackageShare("robolaunch_cloudy_simulator"), "worlds", "industrial-warehouse.sdf"]
    )

gazebo_path = PathJoinSubstitution(
        [FindPackageShare("gazebo_ros"), "launch", "gazebo.launch.py"]
    )

description_launch_path = PathJoinSubstitution(
        [FindPackageShare("robolaunch_cloudy_description"), "launch", "description.launch.py"]
    )
x, y, z = LaunchConfiguration('x'), LaunchConfiguration('y'), LaunchConfiguration('z')
yaw = LaunchConfiguration('yaw')

def generate_launch_description():

    return LaunchDescription([

        DeclareLaunchArgument(
            name="vehicle",
            default_value="'cloudy_v2'",
            description="vehicle type"
        ),

        DeclareLaunchArgument(
            name="world",
            default_value="warehouse",
            description="gazebo world name"
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
                'world': playground_world_path,
            }.items(),
            condition=IfCondition(
                PythonExpression(
                    ["'", LaunchConfiguration("world"), "' == 'playground'"]
                )
            ),
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gazebo_path),
            launch_arguments={
                'use_sim_time': str("true"),
                'world': counter_world_path,
            }.items(),
            condition=IfCondition(
                PythonExpression(
                    ["'", LaunchConfiguration("world"), "' == 'warehouse'"]
                )
            ),
        ),
         
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-topic', 'robot_description',
                       '-entity', 'my_bot',
                       '-x','-3',
                       '-y','-6'
                       ],
            output='screen')
    ])