#!/usr/bin/env python3
# Copyright 2021 Samsung Research America
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration
import time
import copy
import math

"""
Basic navigation demo to go to pose.
"""
time.sleep(5)

# Quaternion class
class Quaternion:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.w = 0.0



# A function that converts euler angles to quaternions
def euler_to_quaternion(roll=0, pitch=0, yaw=0):
    # Abbreviations for the various angular functions
    cy = math.cos(yaw * 0.5)
    sy = math.sin(yaw * 0.5)
    cr = math.cos(roll * 0.5)
    sr = math.sin(roll * 0.5)
    cp = math.cos(pitch * 0.5)
    sp = math.sin(pitch * 0.5)

    q = Quaternion()
    q.w = cy * cr * cp + sy * sr * sp
    q.x = cy * sr * cp - sy * cr * sp
    q.y = cy * cr * sp + sy * sr * cp
    q.z = sy * cr * cp - cy * sr * sp
    return q

def set_angle(pose, yaw):
    q = euler_to_quaternion(0, 0, yaw)
    pose.pose.orientation.x = q.x
    pose.pose.orientation.y = q.y
    pose.pose.orientation.z = q.z
    pose.pose.orientation.w = q.w
    return pose

def draw_rect(h, w, navigator):
    goal_pose = PoseStamped()
    goal_pose.header.frame_id = 'map'
    goal_pose.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose.pose.position.x = 0.0
    goal_pose.pose.position.y = 0.0
    goal_pose.pose.orientation.w = 1.0

    h, w = float(h), float(w)
    
    goal_poses = []
    for _ in range(4):
        goal_poses.append(copy.deepcopy(goal_pose))

    goal_poses[0].pose.position.x = h
    goal_poses[0].pose.position.y = 0.0
    goal_poses[0] = set_angle(goal_poses[0], 0.0)

    goal_poses[1].pose.position.x = h
    goal_poses[1].pose.position.y = w
    goal_poses[1] = set_angle(goal_poses[1], 90.0)

    goal_poses[2].pose.position.x = 0.0
    goal_poses[2].pose.position.y = w
    goal_poses[2] = set_angle(goal_poses[2], 180.0)

    goal_poses[3].pose.position.x = 0.0
    goal_poses[3].pose.position.y = 0.0
    goal_poses[3] = set_angle(goal_poses[3], 270.0)

    print("------- GOAL POSES -------")
    for pose in goal_poses:
        print(pose, end="\n\n")

    return goal_poses

def follow_path(navigator):
    goal_pose = PoseStamped()
    goal_pose.header.frame_id = 'map'
    goal_pose.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose.pose.position.x = 0.0
    goal_pose.pose.position.y = 0.0
    goal_pose.pose.orientation.w = 1.0

    
    goal_poses = []
    for _ in range(10):
        goal_poses.append(copy.deepcopy(goal_pose))

    goal_poses[0].pose.position.x = 0.0
    goal_poses[0].pose.position.y = -4.0
    goal_poses[0] = set_angle(goal_poses[0], 0.0)

    goal_poses[1].pose.position.x = 0.0
    goal_poses[1].pose.position.y = -8.0
    goal_poses[1] = set_angle(goal_poses[1], 0.0)

    goal_poses[2].pose.position.x = -4.0
    goal_poses[2].pose.position.y = -8.0
    goal_poses[2] = set_angle(goal_poses[2], 90.0)

    goal_poses[3].pose.position.x = -4.0
    goal_poses[3].pose.position.y = -4.0
    goal_poses[3] = set_angle(goal_poses[3], 180.0)

    goal_poses[4].pose.position.x = -4.0
    goal_poses[4].pose.position.y = 0.0
    goal_poses[4] = set_angle(goal_poses[4], 270.0)

    goal_poses[5].pose.position.x = -4.0
    goal_poses[5].pose.position.y = 4.0
    goal_poses[5] = set_angle(goal_poses[5], 270.0)

    goal_poses[6].pose.position.x = -4.0
    goal_poses[6].pose.position.y = 9.5
    goal_poses[6] = set_angle(goal_poses[6], -90.0)

    goal_poses[7].pose.position.x = 1.5
    goal_poses[7].pose.position.y = 8.3
    goal_poses[7] = set_angle(goal_poses[7], -90.0)

    goal_poses[8].pose.position.x = 0.0
    goal_poses[8].pose.position.y = 4.0
    goal_poses[8] = set_angle(goal_poses[8], -90.0)

    goal_poses[9].pose.position.x = 0.0
    goal_poses[9].pose.position.y = 0.0
    goal_poses[9] = set_angle(goal_poses[9], -90.0)


    print("------- GOAL POSES -------")
    for pose in goal_poses:
        print(pose, end="\n\n")

    return goal_poses


def main():
    rclpy.init()

    navigator = BasicNavigator()

    # Set our demo's initial pose
    initial_pose = PoseStamped()
    initial_pose.header.frame_id = 'map'
    initial_pose.header.stamp = navigator.get_clock().now().to_msg()
    initial_pose.pose.position.x = 0.0
    initial_pose.pose.position.y = 0.0
    initial_pose.pose.orientation.z = 0.0
    initial_pose.pose.orientation.w = 1.0
    navigator.setInitialPose(initial_pose)

    # Activate navigation, if not autostarted. This should be called after setInitialPose()
    # or this will initialize at the origin of the map and update the costmap with bogus readings.
    # If autostart, you should `waitUntilNav2Active()` instead.
    # navigator.lifecycleStartup()
    print("Waiting for Nav2 to activate...")

    # Wait for navigation to fully activate, since autostarting nav2


    # navigator.waitUntilNav2Active()
    print("Nav2 activated!")

    # If desired, you can change or load the map as well
    # navigator.changeMap('/path/to/map.yaml')

    # You may use the navigator to clear or obtain costmaps
    # navigator.clearAllCostmaps()  # also have clearLocalCostmap() and clearGlobalCostmap()
    # global_costmap = navigator.getGlobalCostmap()
    # local_costmap = navigator.getLocalCostmap()

    # Go to our demos first goal pose
    goal_poses = follow_path(navigator)

    

    # sanity check a valid path exists
    # path = navigator.getPath(initial_pose, goal_pose1)

    for goal in goal_poses:
        navigator.goToPose(goal)

        i = 0
        while not navigator.isTaskComplete():
            ################################################
            #
            # Implement some code here for your application!
            #
            ################################################

            # Do something with the feedback
            i = i + 1
            feedback = navigator.getFeedback()
            if feedback and i % 5 == 0:
                print('Estimated time of arrival: ' + '{0:.0f}'.format(
                    Duration.from_msg(feedback.estimated_time_remaining).nanoseconds / 1e9)
                    + ' seconds.')

                # Some navigation timeout to demo cancellation
                if Duration.from_msg(feedback.navigation_time) > Duration(seconds=600.0):
                    navigator.cancelTask()

                # Some navigation request change to demo preemption
            

    # Do something depending on the return code
    result = navigator.getResult()
    if result == TaskResult.SUCCEEDED:
        print('Goal succeeded!')
    elif result == TaskResult.CANCELED:
        print('Goal was canceled!')
    elif result == TaskResult.FAILED:
        print('Goal failed!')
    else:
        print('Goal has an invalid return status!')

    #navigator.lifecycleShutdown()

    exit(0)


if __name__ == '__main__':
    main()