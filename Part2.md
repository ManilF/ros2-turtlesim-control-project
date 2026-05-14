Hello!

I don't know how much I should explain, but I'll cover everything that's not trivial.

I'll explain things chronologically:

-I first created the publisher and subscriber side of Turtle_Repeater with a Twist type. Subscriber is calling listener_callback as it was in the tutorial.

-Whenever a message is received, it takes note of the time. This is going to be important in timer_callback...

-...because each 20 ms, the timer_callback evaluates wether it's been more than 70ms since the last message was received. If it is the case then the velocites are set to 0.

-In the other case where it has in fact been less than 70ms since the last message, then it publishes that last message.

-get_time() is a helper and it makes things cleaner overall.


