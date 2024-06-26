import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class Subscriber(Node):
    def __init__(self):
        super().__init__('subscriber')
        self.subscription = self.create_subscription(String,'/node1',self.listener_callback,10)
        self.subscription 

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main():
    rclpy.init()
    subscriber = Subscriber()
    rclpy.spin(subscriber)
    rclpy.shutdown()

if __name__ == '__main__':
    main()