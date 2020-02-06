#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import xbox


joy = xbox.Joystick()

def control():
    pub = rospy.Publisher('contrlXbox', String, queue_size=10)
    rospy.init_node('control', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
    	th = str(joy.leftX())
    	x = str(joy.leftY())
    	msgCtr = x + ',' + th 
        #hello_str = "hello world %s" % rospy.get_time()

        rospy.loginfo(msgCtr)
        pub.publish(msgCtr)
        rate.sleep()


if __name__ == '__main__':
	try:
		control()
	except rospy.ROSInterruptException:
		pass

