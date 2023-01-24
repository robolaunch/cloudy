from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, PythonExpression, Command
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare



def generate_launch_description():

    use_sim_time = LaunchConfiguration('use_sim_time'),
    

    cloudy_v1_urdf_path = PathJoinSubstitution(
        [FindPackageShare('robolaunch_cloudy_description'), 'urdf', 'robots', 'cloudy_v1.urdf.xacro']
    ),

    cloudy_v2_urdf_path = PathJoinSubstitution(
        [FindPackageShare('robolaunch_cloudy_description'), 'urdf', 'robots', 'cloudy_v2.urdf.xacro']
    )

    arcelik_urdf_path = PathJoinSubstitution(
        [FindPackageShare('robolaunch_cloudy_description'), 'urdf', 'robots', 'arcelik', 'mecanum.urdf.xacro']
    )

    
    return LaunchDescription([

        DeclareLaunchArgument(
            name='cloudy_v1_urdf', 
            default_value=cloudy_v1_urdf_path,
            description='URDF path'
        ),

        DeclareLaunchArgument(
            name='cloudy_v2_urdf', 
            default_value=cloudy_v2_urdf_path,
            description='URDF path'
        ),

        DeclareLaunchArgument(
            name='arcelik_urdf', 
            default_value=arcelik_urdf_path,
            description='URDF path'
        ),

        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use sim time if true'),

        DeclareLaunchArgument(
            name="vehicle",
            default_value="'cloudy_v2'",
            description="name of the vehicle"
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': Command(['xacro ', LaunchConfiguration('cloudy_v1_urdf')]), 
                'use_sim_time': use_sim_time
            }],
            condition=IfCondition(PythonExpression([LaunchConfiguration("vehicle"), " == 'cloudy_v1'"]))
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': Command(['xacro ', LaunchConfiguration('cloudy_v2_urdf')]), 
                'use_sim_time': use_sim_time
            }],
            condition=IfCondition(PythonExpression([LaunchConfiguration("vehicle"), " == 'cloudy_v2'"]))
        ),

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': Command(['xacro ', LaunchConfiguration('arcelik_urdf')]), 
                'use_sim_time': use_sim_time
            }],
            condition=IfCondition(PythonExpression([LaunchConfiguration("vehicle"), " == 'arcelik'"]))
        ),

        
    ])
