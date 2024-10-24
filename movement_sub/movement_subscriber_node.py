import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from custom_interfaces.msg import CircleMovement

class MovementSubscriber(Node):
    def __init__(self):
        super().__init__("movement_subscriber"); # Initialize node
        self.get_logger().info("Subscriber node is activated!")
        self.subscription = self.create_subscription(CircleMovement, "movement_data", self.subscribeCallback, 10)
    
    def subscribeCallback(self, msg):
        self.get_logger().info(f"I received: linear_x {msg.linear_x}, angular_z: {msg.angular_z}")


def main(args=None):
    # Initialize rclpy
    rclpy.init(args=args)
    # Instantiate node and activate node
    subsrciber_node = MovementSubscriber()
    rclpy.spin(subsrciber_node)
    # Shutdown rclpy
    rclpy.shutdown()

if __name__ == "__main__":
    main()