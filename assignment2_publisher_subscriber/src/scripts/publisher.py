#!/usr/bin/env python
import rospy
from autominy_msgs.msg import NormalizedSteeringCommand , SpeedCommand

steering = 1.0
speed = 0.3

def talker():
	rospy.init_node('talker', anonymous=True)
	steeringPub = rospy.Publisher('/actuators/steering_normalized', NormalizedSteeringCommand, queue_size=10)
	speedPub = rospy.Publisher('/actuators/speed', SpeedCommand, queue_size=10)


	rate = rospy.Rate(10) # 10hz
	while not rospy.is_shutdown():
		steeringOperation = NormalizedSteeringCommand()
		steeringOperation.value = steering
		steeringPub.publish(steeringOperation)
		
		speedOperation = SpeedCommand()
		speedOperation.value = speed
		speedPub.publish(speedOperation)
		
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
