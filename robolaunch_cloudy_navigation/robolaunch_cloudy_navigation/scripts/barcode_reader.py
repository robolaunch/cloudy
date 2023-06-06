#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
import tf2_ros


class BarcodeReader(Node):
    def __init__(self):
        super().__init__('barcode_reader')
        self.barcode_subscription = self.create_subscription(String, 'barcode', self.barcode_callback, 10)
        self.barcode_publisher = self.create_publisher(String, 'barcode_pose', 10)
        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)


    def barcode_callback(self, msg):
        self.t = self.tf_buffer.lookup_transform('map', 'base_link', rclpy.time.Time().to_msg(), rclpy.time.Duration(seconds=1.0))
        self.pose = PoseStamped()
        self.pose.pose.position.x = self.t.transform.translation.x
        self.pose.pose.position.y = self.t.transform.translation.y
        self.pose.pose.position.z = self.t.transform.translation.z
        self.pose.pose.orientation.x = self.t.transform.rotation.x
        self.pose.pose.orientation.y = self.t.transform.rotation.y
        self.pose.pose.orientation.z = self.t.transform.rotation.z
        self.pose.pose.orientation.w = self.t.transform.rotation.w

        json = {
            "barrcode": msg.data,
            "coordinates":
            {
                "x": self.pose.pose.position.x,
                "y": self.pose.pose.position.y
            }
        }

        msg_send = String()
        msg_send.data = str(json) # msg.data + " " + str(self.pose.pose.position.x) + " " + str(self.pose.pose.position.y)
        self.barcode_publisher.publish(msg_send)

if __name__ == '__main__':
    rclpy.init()
    node = BarcodeReader()
    rclpy.spin(node)
    rclpy.shutdown()