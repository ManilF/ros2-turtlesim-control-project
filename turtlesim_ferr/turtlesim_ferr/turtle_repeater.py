import math

from turtlesim.msg import Pose
from turtlesim_ferr_interfaces.srv import SetPose

import rclpy
from rclpy.node import Node 

from geometry_msgs.msg import Twist

class Turtle_Repeater(Node):
    def __init__(self):
        super().__init__('turtle_repeater')

        self.current_x = None
        self.current_y = None 
        self.current_theta = None
        self.last_t_received = None
        self.latest_message = Twist()


        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel_repeat', 10)
        self.subscription = self.create_subscription(Twist, '/turtle1/cmd_vel', self.get_latest_message, 10)
        
        self.timer = self.create_timer(0.05, self.timer_callback)




        # part 3:
        self.pose_subscriber_ = self.create_subscription(Pose, "/turtle1/pose", self.get_current_state, 10)
        self.set_pose_service_ = self.create_service(SetPose, "/set_pose", self.give_directions)

    def get_latest_message(self, message):
        self.latest_message=message
        self.last_t_received = self.get_time()


    def timer_callback(self):
        current_t = self.get_time()
        if self.last_t_received is not None and current_t - self.last_t_received < 0.07 :
            self.publisher_.publish(self.latest_message)
        else :
            rest_message = Twist()
            self.publisher_.publish(rest_message)

            
    def get_time(self):
        return self.get_clock().now().nanoseconds/1e9
    


    def get_current_state(self, message):
        self.current_x = message.x
        self.current_y = message.y
        self.current_theta = message.theta

    def give_directions(self, request, response):
        if self.current_x is None :
            response.distance = 0.0
            response.angle = 0.0
            return response

        dx = request.x - self.current_x
        dy = request.y - self.current_y

        target_angle = math.atan2(dy, dx)
        angle_to_rotate = target_angle - self.current_theta
        angle_to_rotate = math.atan2(math.sin(angle_to_rotate), math.cos(angle_to_rotate))

        response.distance = math.sqrt(dx**2 + dy**2)
        response.angle = angle_to_rotate
        
        return response
            

    




    



def main(args=None):
    rclpy.init(args=args)

    turtle_Repeater = Turtle_Repeater()
    rclpy.spin(turtle_Repeater)

    turtle_Repeater.destroy_node()
    rclpy.shutdown() 


if __name__ == '__main__':
    main()



