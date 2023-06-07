#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
import tf2_ros
import json


class BarcodeReader(Node):
    def __init__(self):
        super().__init__('barcode_reader')
        self.barcode_subscription = self.create_subscription(String, 'barcode', self.barcode_callback, 10)
        self.barcode_publisher0 = self.create_publisher(String, 'barcode_pose0', 10)
        self.barcode_publisher1 = self.create_publisher(String, 'barcode_pose1', 10)
        self.barcode_publisher2 = self.create_publisher(String, 'barcode_pose2', 10)
        self.barcode_publisher3 = self.create_publisher(String, 'barcode_pose3', 10)

        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)
        self.barcode_list = []


    def barcode_callback(self, msg):

        id = msg.data.split("-")[0]
        code = msg.data.split("-")[1]

        if not id in self.barcode_list:
            print("barcode: " + msg.data)
            self.t = self.tf_buffer.lookup_transform('map', 'base_link', rclpy.time.Time().to_msg(), rclpy.time.Duration(seconds=1.0))
            self.pose = PoseStamped()
            self.pose.pose.position.x =    self.t.transform.translation.x
            self.pose.pose.position.y =    self.t.transform.translation.y
            self.pose.pose.position.z =    self.t.transform.translation.z
            self.pose.pose.orientation.x = self.t.transform.rotation.x
            self.pose.pose.orientation.y = self.t.transform.rotation.y
            self.pose.pose.orientation.z = self.t.transform.rotation.z
            self.pose.pose.orientation.w = self.t.transform.rotation.w

            

            json_obj = {
                "barcode": code,
                "coordinates":
                {
                    "x": self.pose.pose.position.x,
                    "y": self.pose.pose.position.y
                }
            }

            msg_send = String()
            msg_send.data = json.dumps(json_obj, ensure_ascii=False )  # str(json_obj) # msg.data + " " + str(self.pose.pose.position.x) + " " + str(self.pose.pose.position.y)

            if   id == "0":
                self.barcode_publisher0.publish(msg_send)
            elif id == "1":
                self.barcode_publisher1.publish(msg_send)
            elif id == "2":
                self.barcode_publisher2.publish(msg_send)
            elif id == "3":
                self.barcode_publisher3.publish(msg_send)

        self.barcode_list.append(id)
        

if __name__ == '__main__':
    rclpy.init()
    node = BarcodeReader()
    rclpy.spin(node)
    rclpy.shutdown()