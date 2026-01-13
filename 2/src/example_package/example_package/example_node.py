#!/usr/bin/python3
import os
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


# Fill in something for msg type imports
# from duckietown_msgs.msg import SOMETHING
# from std_msgs.msg import SOMETHING

class SkeletonNode(Node):
    def __init__(self):
        super().__init__('example_node')
        self.publisher_ = self.create_publisher(
            String,
            'chatter_2',
            10
        )
        self.timer_ = self.create_timer(
            1.0,  # seconds
            self.timer_callback
        )

        self.counter = 0
        self.get_logger().info('Talker node started')

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello ROS2 #{self.counter}'
        self.publisher_.publish(msg)

        self.get_logger().info(f'Published: "{msg.data}"')
        self.counter += 1


def main():
    print('In main')
    rclpy.init()
    node = SkeletonNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
