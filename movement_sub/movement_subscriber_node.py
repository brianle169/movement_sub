import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from custom_interfaces.msg import CircleMovement

class MovementSubscriber(Node):
    def __init__(self):
        super().__init__("movement_subscriber"); # Initialize node
        self.get_logger().info("Subscriber node is activated!")
        self.subscription = self.create_subscription(CircleMovement, "movement_data", self.subscribeCallback, 10)
        # Our subscriber is also a publisher to "turtle1/cmd_vel" topic
        self.publisher_ = self.create_publisher(Twist, "/turtle1/cmd_vel",10)
    
    def subscribeCallback(self, msg):
        self.get_logger().info(f"Received linear_x {msg.linear_x}, angular_z: {msg.angular_z}")
        # Create a new message of type Twist to feed to /turtle1/cmd_vel topic
        message = Twist();
        message.linear.x = msg.linear_x
        message.angular.z = msg.angular_z
        self.get_logger().info(f"Publishing linear_x {msg.linear_x}, angular_z: {msg.angular_z} to /cmd_vel topic. Run \"ros2 run turtlesim turtlesim_node\" to check.")
        self.publisher_.publish(message)
        


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