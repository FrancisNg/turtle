import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class MoveTurtleSquare(Node):

    def __init__(self):
        super().__init__("move_turtle_square")
        self.pose_ = None
        self.target = []
        self.publisher_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.subscriber_ = self.create_subscription(Pose, "turtle1/pose", self.turtlePose_callback, 10)
        self.control_loop_timer_ = self.create_timer(0.01, self.control_loop)
        self.i = 0

    def turtlePose_callback(self, msg):
        self.pose_ = msg


        self.target.append([self.pose_.x + 1.0, self.pose_.y])
        self.target.append([self.pose_.x + 1.0, self.pose_.y + 1.0])
        self.target.append([self.pose_.x, self.pose_.y + 1.0])
        self.target.append([self.pose_.x, self.pose_.y])


    def control_loop(self):
        if (self.pose_ == None):
            return
        
        msg = Twist()

        if abs(self.target[self.i][0] - self.pose_.x == 0) and abs(self.target[self.i][1] - self.pose_.y == 0):
            if (self.i > 3):
                self.i = 0
            else:
                self.i += 1
        else:
            msg.linear.x = self.target[self.i][0] - self.pose_.x
            msg.linear.y = self.target[self.i][1] - self.pose_.y
        
        self.publisher_.publish(msg)
        
def main(args=None):
    rclpy.init(args=args)
    move_turtle_square = MoveTurtleSquare()
    rclpy.spin(move_turtle_square)
    move_turtle_square.destroy_node()
    rclpy.shutdown()
    
       
if __name__ == "__main__":
	main()

