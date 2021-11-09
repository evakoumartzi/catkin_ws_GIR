#!/usr/bin/env python
import rospy
from autominy_msgs.msg import Speed

def callback (data):
	print(data.value)

def listener():

     rospy.init_node('listener', anonymous=True)

     rospy.Subscriber("/sensors/speed", Speed, callback)

     rospy.spin()

if __name__ == '__main__':
     listener()
