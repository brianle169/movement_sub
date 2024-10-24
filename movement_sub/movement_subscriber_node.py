import rclpy
from rclpy import Node

class MovementSubscriber(Node):
    def __init__(self):
        super.__init__("movement_subscriber"); # Initialize node


def main(args=None):
    # Initialize rclpy
    rclpy.init(args)
    # Shutdown rclpy
    rclpy.shutdown()

if __name__ == "__main__":
    main()