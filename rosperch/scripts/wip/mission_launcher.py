#!/usr/bin/env python3
# Based on the simple publisher/subscriber tutorial on the ROS tutorial page:
# https://github/ros/ros_tutorials.com
# And the UTAP 2020 Code at https://github.com/jdicecco/UTAP/blob/master/UTAP_2020.py
# Software License Agreement (BSD License)

import rospy
import time
from std_msgs.msg import Bool

def talker():
    pub = rospy.Publisher('motorstuff', Bool, queue_size=10) # Publish to motorstuff topic
    rospy.init_node('talker', anonymous=True) # Initiate talker node
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        command_input = float(input("Launch mission? (1/0): ")) # Query for command and convert to float
        launch_command = bool(command_input) # Convert to boolean
        print("launch_command is : %s" % launch_command)
        rospy.loginfo(launch_command) # Log the entered command
        pub.publish(launch_command) # Publish command to ledstuff topic
        rate.sleep() # Sleep (10ms)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
