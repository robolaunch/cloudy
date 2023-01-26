#!/usr/bin/env python3
import rclpy

from rclpy.node import Node
import serial
from struct import pack,unpack
from .MecanumControllib.MecanumControllib import *
import os
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import JointState





#ser.write((""+ "\n").encode()) #Clearing serial buffer
#line = read_serial(ser)
#print("Recieved"+line)


class SerialNode(Node):

    def __init__(self):
        super().__init__('serial_node')

        self.SERIAL_PORT = '/dev/ttyUSB0'
        self.ser = serial.Serial(self.SERIAL_PORT,115200)
        
        self.publisher_ = self.create_publisher(Odometry, 'wheel/odometry', 10)
        self.joint_pub = self.create_publisher( JointState, "joint_states", 10)
        timer_period = 0.004  # seconds
        self.odom_msg = Odometry()
        self.odom_msg.header.frame_id = "odom"
        self.odom_msg.child_frame_id = "base_link"
        self.timer = self.create_timer(timer_period, self.arduino_callback)
        #self.timer_j = self.create_timer(0.001, self.joint_callback)

        self.counter = 0
        self.init_time = self.get_clock().now()
        self.is_initialized = False
        self.create_subscription(Twist,'cmd_vel',self.cmd_vel_callback,10)
        self.mecanum_controller = MecanumControl(80,430,500,-5000,5000)
        self.joint_state = JointState()
        self.joint_state.name.extend(["front_left_wheel_joint","front_right_wheel_joint","rear_left_wheel_joint","rear_right_wheel_joint"])
        self.joint_state.position.extend([0,0,0,0])
        self.joint_state.velocity.extend([0,0,0,0])
        self.joint_state.effort.extend([0,0,0,0])
        
    """ def joint_callback(self):
       
        if(self.mecanum_controller.front_left_motor_speed > 0.01 or self.mecanum_controller.front_left_motor_speed < -0.01):
            self.joint_state.position[0] = (-3.14)+((self.joint_state.position[0]-self.mecanum_controller.front_left_motor_speed*0.0001)% (6.28))
        if(self.mecanum_controller.front_right_motor_speed > 0.01 or self.mecanum_controller.front_right_motor_speed < -0.01):
            self.joint_state.position[1] = (-3.14)+((self.joint_state.position[1]+self.mecanum_controller.front_right_motor_speed*0.0001)% (6.28))
        if(self.mecanum_controller.back_left_motor_speed > 0.01 or self.mecanum_controller.back_left_motor_speed < -0.01):
            self.joint_state.position[2] = (-3.14)+((self.joint_state.position[2]-self.mecanum_controller.back_left_motor_speed*0.0001)% (6.28))
        if(self.mecanum_controller.back_right_motor_speed > 0.01 or self.mecanum_controller.back_right_motor_speed < -0.01):
            self.joint_state.position[3] = (-3.14)+((self.joint_state.position[3]+self.mecanum_controller.back_right_motor_speed*0.0001)% (6.28))

        self.joint_state.header.stamp = self.get_clock().now().to_msg()
        self.joint_pub.publish(self.joint_state) """

    def arduino_callback(self):

        if(self.ser.in_waiting >= 45):            
            
            float_data = unpack('<11fc',self.ser.read(45))
            #self.get_logger().info('x'+str(float_data[9])+" "+str(float_data[10]))
            self.odom_msg.header.stamp = self.get_clock().now().to_msg()
            
            self.odom_msg.pose.pose.position.x = float_data[1]
            self.odom_msg.pose.pose.position.y = float_data[0]
            self.odom_msg.pose.pose.position.z = 0.0

            self.odom_msg.pose.pose.orientation.x = float_data[2]
            self.odom_msg.pose.pose.orientation.y = float_data[3]
            self.odom_msg.pose.pose.orientation.z = float_data[4]
            self.odom_msg.pose.pose.orientation.w = float_data[5]

            self.odom_msg.pose.covariance[0] = 0.001
            self.odom_msg.pose.covariance[7] = 0.001
            self.odom_msg.pose.covariance[35] = 0.001

            self.odom_msg.twist.twist.linear.x = float_data[7]*0.1297
            self.odom_msg.twist.twist.linear.y = float_data[6]*0.1297
            self.odom_msg.twist.twist.linear.z = 0.0

            self.odom_msg.twist.twist.angular.x = 0.0
            self.odom_msg.twist.twist.angular.y = 0.0
            self.odom_msg.twist.twist.angular.z = float_data[8]

            self.odom_msg.twist.covariance[0] = 0.0001
            self.odom_msg.twist.covariance[7] = 0.0001
            self.odom_msg.twist.covariance[35] = 0.0001

            self.publisher_.publish(self.odom_msg)
            self.mecanum_controller.calculateMecanum(float_data[6],float_data[7],float_data[8])


            """ if(self.mecanum_controller.front_left_motor_speed > 0.01 or self.mecanum_controller.front_left_motor_speed < -0.01):
                self.joint_state.position[0] = (-3.14)+((self.joint_state.position[0]-self.mecanum_controller.front_left_motor_speed*0.0001)% (3.14))
            if(self.mecanum_controller.front_right_motor_speed > 0.01 or self.mecanum_controller.front_right_motor_speed < -0.01):
                self.joint_state.position[1] = (-3.14)+((self.joint_state.position[1]+self.mecanum_controller.front_right_motor_speed*0.0001)% (3.14))
            if(self.mecanum_controller.back_left_motor_speed > 0.01 or self.mecanum_controller.back_left_motor_speed < -0.01):
                self.joint_state.position[2] = (-3.14)+((self.joint_state.position[2]-self.mecanum_controller.back_left_motor_speed*0.0001)% (3.14))
            if(self.mecanum_controller.back_right_motor_speed > 0.01 or self.mecanum_controller.back_right_motor_speed < -0.01):
                self.joint_state.position[3] = (-3.14)+((self.joint_state.position[3]+self.mecanum_controller.back_right_motor_speed*0.0001)% (3.14))

            
            self.joint_state.header.stamp = self.get_clock().now().to_msg()
            self.joint_pub.publish(self.joint_state) """

            

    def cmd_vel_callback(self,msg):
        if(self.is_initialized):
            self.ser.write(pack('6f',msg.linear.x * 9.3,msg.linear.y * 9.3,msg.linear.z,msg.angular.x,msg.angular.y,msg.angular.z * 4.2))
        elif(((self.get_clock().now() - self.init_time).nanoseconds * 1e-9) >= 1):
            self.is_initialized = True


def main(args=None):
    rclpy.init(args=args)

    serial_node = SerialNode()

    rclpy.spin(serial_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    serial_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
