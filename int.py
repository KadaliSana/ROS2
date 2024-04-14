import rclpy
from rclpy.node import Node

from tutorial_interfaces.msg import Num

class Publisher(Node):

    def __init__(self):
        super().__init__('publisher')
        self.two_publisher_ = self.create_publisher(Num, '/data_twos', 10)
        self.five_publisher_ = self.create_publisher(Num, '/data_fives', 10)
        self.num1=0
        self.num2=0
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Num()
        msg.num1=self.num1
        self.num1 *=2
        msg.num2=self.num2
        self.num2 *=5
        self.two_publisher_.publish(msg)
        self.five_publisher_.publish(msg)
        self.get_logger().info('Publishing: num1= %d, num2=%d'%(msg.num1,msg.num2))

def main():
    rclpy.init()
    publisher = Publisher()
    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()