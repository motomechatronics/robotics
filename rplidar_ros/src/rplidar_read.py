#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
  rospy.loginfo("distance at 180 deg is "+str(msg.ranges[180]))

rospy.init_node('scan_node', log_level=rospy.DEBUG)
rate=rospy.Rate(10)
pub = rospy.Subscriber('/scan',LaserScan,callback)
while not rospy.is_shutdown():
   rate.sleep()
