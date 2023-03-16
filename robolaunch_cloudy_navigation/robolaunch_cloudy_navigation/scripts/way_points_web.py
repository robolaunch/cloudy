#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
from rclpy.duration import Duration
import time
import copy
import math
import tf2_ros
import os

class WayPointsWeb(Node):

    def __init__(self):
        super().__init__('way_points_web')
        self.get_logger().info("WayPointsWeb node has been started")
        self.way_points = []

        self.navigator = BasicNavigator()

        # Set our demo's initial pose
        initial_pose = PoseStamped()
        initial_pose.header.frame_id = 'map'
        initial_pose.header.stamp = self.navigator.get_clock().now().to_msg()
        initial_pose.pose.position.x = 0.0
        initial_pose.pose.position.y = 0.0
        initial_pose.pose.orientation.z = 0.0
        initial_pose.pose.orientation.w = 1.0

        self.t = tf2_ros.TransformStamped()
        self.pose = PoseStamped()

        self.navigator.setInitialPose(initial_pose)

        time.sleep(5)

        self.subscription = self.create_subscription(String, 'way_points_web', self.waypoints_callback, 10)
        self.pose_publisher = self.create_publisher(PoseStamped, 'robot_position', 10)

        # create tf2 buffer and listener
        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)


        self.create_timer(0.1, self.timer_callback)


    def timer_callback(self):
        
        self.publish_robot_position()

    def publish_robot_position(self):
        self.t = self.tf_buffer.lookup_transform('odom', 'base_link', rclpy.time.Time().to_msg(), rclpy.time.Duration(seconds=1.0))
        self.pose = PoseStamped()
        self.pose.pose.position.x = self.t.transform.translation.x
        self.pose.pose.position.y = self.t.transform.translation.y
        self.pose.pose.position.z = self.t.transform.translation.z
        self.pose.pose.orientation.x = self.t.transform.rotation.x
        self.pose.pose.orientation.y = self.t.transform.rotation.y
        self.pose.pose.orientation.z = self.t.transform.rotation.z
        self.pose.pose.orientation.w = self.t.transform.rotation.w

        self.pose_publisher.publish(self.pose)


    def waypoints_callback(self, msg):

        self.get_logger().info("Waypoint received")

        points = msg.data.split("/")
        
        waypoints = []
        for i in range(len(points)):
            x = float(points[i])
            y = float(points[i+1])
            

            goal_pose = PoseStamped()
            goal_pose.header.frame_id = 'map'
            goal_pose.header.stamp = self.get_clock().now().to_msg()
            goal_pose.pose.position.x = x
            goal_pose.pose.position.y = y
            goal_pose.pose.orientation.w = 1.0

            waypoints.append(goal_pose)

            i += 1
            if i == len(points)-1:
                break


        for goal in waypoints:
            self.navigator.goToPose(goal)

            i = 0
            while not self.navigator.isTaskComplete():
                
                self.publish_robot_position()
                # rclpy.spin_once(self, timeout_sec=0.01)  

                # Do something with the feedback
                i = i + 1
                feedback = self.navigator.getFeedback()
                if feedback and i % 5 == 0:
                    print('Estimated time of arrival: ' + '{0:.0f}'.format(
                        Duration.from_msg(feedback.estimated_time_remaining).nanoseconds / 1e9)
                        + ' seconds.')

                    # Some navigation timeout to demo cancellation
                    if Duration.from_msg(feedback.navigation_time) > Duration(seconds=600.0):
                        self.navigator.cancelTask()

                    # Some navigation request change to demo preemption
                

        # Do something depending on the return code
        result = self.navigator.getResult()
        if result == TaskResult.SUCCEEDED:
            print('Goal succeeded!')
        elif result == TaskResult.CANCELED:
            print('Goal was canceled!')
        elif result == TaskResult.FAILED:
            print('Goal failed!')
        else:
            print('Goal has an invalid return status!')

        #navigator.lifecycleShutdown()



def main(args=None):
    rclpy.init(args=args)

    way_points_web = WayPointsWeb()

    rclpy.spin(way_points_web)

    way_points_web.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()