#!/usr/bin/env python  
import rospy

from std_msgs.msg import Int16
from project1_solution.msg import TwoInts

def callback(intsum):
 	rospy.loginfo(rospy.get_caller_id()+"I heard %s", intsum.a + intsum.b)
  
def listener():
 	msg = TwoInts
 	rospy.init_node('listener', anonymous=True)
  	rospy.subscribe("two_ints", msg, callback)
    rospy.spin()
    
if _name_ == '_main_':
 	listener()