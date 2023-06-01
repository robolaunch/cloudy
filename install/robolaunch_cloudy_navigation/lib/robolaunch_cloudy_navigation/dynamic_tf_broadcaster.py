#!/usr/bin/env python3
from geometry_msgs.msg import TransformStamped

import rclpy
from rclpy.node import Node

from tf2_ros import TransformBroadcaster
from nav_msgs.msg import Odometry

class FixedFrameBroadcaster(Node):

    def __init__(self):
        super().__init__('fixed_frame_tf2_broadcaster')

        self.tf_broadcaster = TransformBroadcaster(self)
        self.timer = self.create_timer(0.1, self.broadcast_timer_callback)
        self.create_subscription(Odometry, '/odom', self.odometry_callback, 10)
        self.odometry = Odometry()
        self.odometry.pose.pose.orientation.w = 1.0

        print(self.odometry.pose.pose.orientation)


    def broadcast_timer_callback(self):
        # self.static_tf_handle("map", "odometry")
        self.static_tf_handle("map", "foo")
        # self.static_tf_handle("odom", "base_footprint")


        # self.dynamic_tf_handle("odom", "base_footprint")

        # self.static_tf_handle("base_footprint", "base_link")
        # self.static_tf_handle("base_link", "laser")


        # self.dynamic_tf_handle("base_footprint", "base_link")
        # self.dynamic_tf_handle("base_link", "camera_link")  
        pass 

    def dynamic_tf_handle(self, name, child):
        t = TransformStamped()

        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = name
        t.child_frame_id = child

        t.transform.translation.x = 0.0
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0

        if self.odometry.pose.pose.orientation.x == 0.0 and self.odometry.pose.pose.orientation.y == 0.0:

            t.transform.rotation.x = 0.0
            t.transform.rotation.y = 0.0
            t.transform.rotation.z = 0.0
            t.transform.rotation.w = 1.0
        else:
            
            t.transform.rotation.x = float(self.odometry.pose.pose.orientation.x)
            t.transform.rotation.y = float(self.odometry.pose.pose.orientation.y)
            t.transform.rotation.z = float(self.odometry.pose.pose.orientation.z)
            t.transform.rotation.w = float(self.odometry.pose.pose.orientation.w)

            t.transform.translation.x = float(self.odometry.pose.pose.position.x)
            t.transform.translation.x = float(self.odometry.pose.pose.position.y)
            t.transform.translation.x = float(self.odometry.pose.pose.position.z)


        self.tf_broadcaster.sendTransform(t)

    def static_tf_handle(self, name, child):
        t = TransformStamped()

        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = name
        t.child_frame_id = child
        t.transform.translation.x = 0.0
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0


        self.tf_broadcaster.sendTransform(t)

    def odometry_callback(self, msg):
        self.odometry = msg

def main():
    print("-")
    rclpy.init()
    node = FixedFrameBroadcaster()
    print("Starting broadcaster")
    rclpy.spin(node)
    print("Stopping broadcaster")
    rclpy.shutdown()

main()