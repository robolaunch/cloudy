#!/usr/bin/env python3
import rclpy


from threading import Event
from .MecanumControllib.MecanumControllib import *
from rclpy.node import Node
from rclpy.duration import Duration
from geometry_msgs.msg import Twist
import odrive

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        
        self.thread_permission = Event()
        self.prev_time = self.get_clock().now()
        self.subs_msg = Twist()
        self.thread_permission.set()

        #self.publisher_ = self.create_publisher(TwistStamped, 'cmd_vel', 10)
        timer_period = 0.001  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.mecanum_controller = MecanumControl(80,430,500,-5000,5000)
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.odrives = odrive.find_any() 
        #self.get_logger().info('ODRIVEFOUND FOUND' +str(self.odrives))
        
    def listener_callback(self, msg):
        
        self.thread_permission.wait()
        self.thread_permission.clear()

        self.prev_time = self.get_clock().now()
        self.subs_msg = msg
        #self.get_logger().info('SUBSCRIBER ACTIVATED' +str(self.prev_time))

        self.thread_permission.set()
        #self.odrv0.axis0.set_input_vel = self.mecanum_controller.getMotorSpeed(0)
        #self.odrv0.axis1.set_input_vel = self.mecanum_controller.getMotorSpeed(1)
        #self.odrv1.axis0.set_input_vel = self.mecanum_controller.getMotorSpeed(2)
        #self.odrv1.axis1.set_input_vel = self.mecanum_controller.getMotorSpeed(3)

    def timer_callback(self):
        self.thread_permission.wait()
        self.thread_permission.clear()
        
        #self.get_logger().info(str((self.get_clock().now() - self.prev_time).to_msg()))
        msg = self.subs_msg
        self.thread_permission.set()
        #self.publisher_.publish(msg)
        self.mecanum_controller.calculateMecanum(msg.linear.x,msg.linear.y,msg.angular.z)
        self.get_logger().info(str(self.mecanum_controller.getCalculatedMotorSpeed(0)))
        self.odrives.axis0.controller.input_vel = self.mecanum_controller.getCalculatedMotorSpeed(0)
        self.get_logger().info('Sensorless estimate' + str(self.odrives.axis0.sensorless_estimator.vel_estimate))
        self.get_logger().info('Vel estimate' + str(self.odrives.axis0.encoder.vel_estimate))

        #TODO max min limitlerini belirleme
        #Angular dengeleme
        #Serialler ile odrivelarin on arka ayrimini yapma
        #Odometry deneme ve publishleme
        #msg.linear.y = self.mecanum_controller.getCalculatedMotorSpeed(1)
        #msg.linear.z = self.mecanum_controller.getCalculatedMotorSpeed(2)
        #msg.angular.x = self.mecanum_controller.getCalculatedMotorSpeed(3)
        #msg.angular.y = 0.0
        #msg.angular.z = 0.0

        #self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    
    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()