import rclpy
from rclpy import Node

def main(args=None):
    # Initialize rclpy
    rclpy.init(args)
    # Shutdown rclpy
    rclpy.shutdown()

if __name__ == "__main__":
    main()