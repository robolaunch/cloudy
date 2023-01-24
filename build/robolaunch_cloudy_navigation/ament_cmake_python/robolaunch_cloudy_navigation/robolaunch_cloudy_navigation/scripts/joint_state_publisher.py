import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

class JointStatePublisher(Node):
    
    def __init__(self):
        super().__init__('joint_state_publisher')
        self.get_logger().info('Joint State Publisher has been started')
        self.joint_names = ['base_footprint', 'base_link', 'camera_link', 'front_caster_wheel_link', 
        'imu_link', 'laser', 'rear_caster_wheel_link', 'left_wheel_link', 'right_wheel_link', 'camera_depth_link']
        self.publisher = self.create_publisher(JointState, "/joint_states", 10)
        self.create_timer(0.1, self.timer_callback)

    def publish_joint_states(self):
        joint_state = JointState()
        joint_state.header.stamp = self.get_clock().now().to_msg()
        joint_state.name = self.joint_names
        joint_state.position = [1.0] * len(self.joint_names)
        joint_state.velocity = [1.0] * len(self.joint_names)
        self.publisher.publish(joint_state)

    # def publish_joint_states(self):
    #     joint_state = JointState()
    #     joint_state.header.stamp = self.get_clock().now().to_msg()
    #     joint_state.name = ["left_wheel_joint", "right_wheel_joint"]
    #     joint_state.position = [1.0, 1.0]
    #     joint_state.velocity = [1.0, 1.0]
    #     self.publisher.publish(joint_state)

    def timer_callback(self):
        self.publish_joint_states()

if __name__ == "__main__":
    rclpy.init()
    joint_state_publisher = JointStatePublisher()
    rclpy.spin(joint_state_publisher)
    rclpy.shutdown(joint_state_publisher)