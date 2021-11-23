#!/usr/bin/env python
import rospy
from sensor_msgs.msg import CameraInfo , Image

def callback (data):
	print("\nintrinsic parameters:")
	print("fx = ",data.K[0])
	print("fy = ",data.K[4])
	print("cx = ",data.K[2])
	print("cy = ",data.K[5])
	print("\ndistortion coefficients:")
	print("k1 = ",data.D[0])
	print("k2 = ",data.D[1])
	print("t1 = ",data.D[2])
	print("t2 = ",data.D[3])
	print("k3 = ",data.D[4])

def savefile (data):
	name = ".~/catkin_ws_GIR/src/assignment4_test/images/image.png"
	with open("/home/pecco/saveimage", "wb") as f:
	    data.serialize(f)
	#print("\nthe image is saved under: ",name)
	

def listener():

     rospy.init_node('listener', anonymous=True)
     rospy.Subscriber("/sensors/camera/infra1/camera_info", CameraInfo, callback)
     rospy.Subscriber("/sensors/camera/infra1/image_rect_raw", Image, savefile)

     rospy.spin()

if __name__ == '__main__':
     listener()
