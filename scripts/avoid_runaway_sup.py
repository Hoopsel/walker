#!/usr/bin/env python
# coding=utf-8

import rospy
import time
from geometry_msgs.msg import Twist

time1 = 0.0

def avoidCB(msg):  
    global time1
    print("avoidCB start")
    time1 = time.time()
    pub1 = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=10)
    pub1.publish(msg)    

def runawayCB(msg):
    global time1
    print("runawayCB start!")
    time2 = time.time()
    pub1 = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=10)
    if (time2 - time1) > 0.5:
        pub1.publish(msg)
        print("avoid node broke down, runaway node pulish successfully!")

def main():
    rospy.init_node('avoid_runaway_sup', anonymous=True)
    sub1 = rospy.Subscriber("/avoid_cmd_vel", Twist, avoidCB)
    sub2 = rospy.Subscriber("/runaway_cmd_vel", Twist, runawayCB)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
