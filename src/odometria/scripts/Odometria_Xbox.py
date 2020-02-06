#! /usr/bin/env python

from tf import TransformBroadcaster
import tf
import rospy
from rospy import Time 
from std_msgs.msg import String
import xbox
import math

joy = xbox.Joystick()

def main():
    rospy.init_node('Odometria_Xbox')
    
    b = TransformBroadcaster()
    
    translation = (0.0, 0.0, 0.0)
    rotation = (0.0, 0.0, 0.0, 1.0) #quaternion
    rate = rospy.Rate(5)  # 5hz

    yant = 0.0
    xant = 0.0
    
    while not rospy.is_shutdown():
    	#y = math.degrees(math.asin(joy.leftX())) #+ yant
        y = joy.leftX() + yant
    	x = joy.leftY() + xant

        translation = (x, 0.0, 0.0)
        rotation = tf.transformations.quaternion_from_euler(0, 0, y)

        yant = y
        xant = x
	
	#print(y)
        
        b.sendTransform(translation, rotation, Time.now(), 'camera_link', 'odom')
        rate.sleep()

if __name__ == '__main__':
    main()
