# Part 3

As required, I created a seperate interface package to define the "SetPose" Service (which contains a target x and y position as well as a response that returns the min distance between the targer and the current position of the turtle). The nodes is subscribed to '/Turle1/pose' so it continuously stores the turtle's current position.


As of the code:
1- I initialized the current state variables of the turtle (x,y, and theta)
2- Then I created a subscriber that runs get_current_state whenever a new pose arrives, and a service server that runs the callback whenever a client sends a request.
3- give_direction is quite trivial except lines 67 and 69 which I will explain. First I started making the calculations with atan then I realized it will only give values ranging from pi/2 to -pi/2 (whereas atan->-pi to pi). Line 69 is a way to normalize the angle to (-pi,pi] since the difference of angles can be outside of that range.