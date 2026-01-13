#!/usr/bin/python3
import rclpy
from std_msgs.msg import String
from rclpy.node import Node


class SimpleNode(Node):
    def __init__(self):
        super().__init__('simple_node')

        self.sub = self.create_subscription(String, 'chatter', self.callback_function, 10)  # create subscriber

        self.publish()

    def callback_function(self, msg):  # receive massage
        self.get_logger().info('I heard: "%s"' % msg.data)  # parce it


def main():
    rclpy.init()
    node = SimpleNode()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
