import os
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([  
        Node(
            package='cv_basics',
            namespace='cv_basics',
            executable='webcam_pub',
            name='webcam_pub',
        ),
        Node(
            package='image_transport',
            executable='republish',
            name='republish',
            namespace='cv_basics',
            arguments=['raw','compressed'],
            remappings=[
                ('in', '/camera/image/image_raw'),
                ('out', '/target/compressed')
            ]
        )               
])

# # raw compressed --ros-args --remap in:=/camera/image/image_raw --remap out/compressed:=/target/compressed
