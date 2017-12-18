#!/usr/bin/env python

import rospy
from sensor_msgs.msg import NavSatFix

rospy.init_node("edit_gps_frame_id_node")

gps_pub = rospy.Publisher("gps/fix", NavSatFix, queue_size=10)

def gps_callback(data):
	new_gps = NavSatFix()
	new_gps = data
	new_gps.header.frame_id = "gps"
	gps_pub.publish(new_gps)

if __name__=="__main__":
	rospy.Subscriber("fix", NavSatFix, gps_callback)
	try:
		while not rospy.is_shutdown():
			pass
	except rospy.ROSInterruptException:
		pass