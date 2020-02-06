#! /usr/bin/env python

from tf import TransformBroadcaster
import rospy
from rospy import Time 
from std_msgs.msg import String


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "%s", data.data)
    x,th = data.data.split(',')

    b = TransformBroadcaster()

    translation = (0.0, 0.0, 0.0)
    rotation = (0.0, 0.0, 0.0, 0.0)

    #rate = rospy.Rate(5)  # 5hz
        
    x = float(x)
    th = float(th)
    
    translation = (x, 0.0, 0.0)
    rotation = (0.0, 0.0, 0.0, th)
    
    b.sendTransform(translation, rotation, Time.now(), 'Raiden', '/world')
    #rate.sleep()

def main():

    rospy.init_node('OdometrySilver')
    rospy.Subscriber("contrlXbox", String, callback)
    rospy.spin()
    

if __name__ == '__main__':
    main()
