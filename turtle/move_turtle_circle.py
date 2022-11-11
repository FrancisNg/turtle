import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class MoveTurtleCircle(Node):

    def __init__(self):
        super().__init__("move_turtle_circle")
        self.pose_ = None
        self.publisher_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.subscriber_ = self.create_subscription(Pose, "turtle1/pose", self.turtlePose_callback, 10)
        self.control_loop_timer_ = self.create_timer(0.01, self.control_loop)
        self.i = 0

    def turtlePose_callback(self, msg):
        self.pose_ = msg

    def control_loop(self):
        if (self.pose_ == None):
            return
        
        msg = Twist()

        msg.linear.x = 2.0
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 1.8
        
        self.publisher_.publish(msg)
        
def main(args=None):
    rclpy.init(args=args)
    move_turtle_circle = MoveTurtleCircle()
    rclpy.spin(move_turtle_circle)
    move_turtle_circle.destroy_node()
    rclpy.shutdown()
    
       
if __name__ == "__main__":
	main()

