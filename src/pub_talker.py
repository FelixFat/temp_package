import rospy
from std_msgs.msg import String
import time

if __name__ == '__main__':
    rospy.init_node('pub_talker', anonymous = True)
    pub = rospy.Publisher('chatter', String, queue_size = 10)
    rate = rospy.Rate(10)
        
    try:
        while not rospy.is_shutdown():
            time_tuple = time.localtime()
            time_string = time.strftime('%H:%M:%S', time_tuple)
            
            message = 'Hello World! Time: %s' %(time_string)
            rospy.loginfo(message)
            pub.publish(message)
            
            rate.sleep()
    except rospy.ROSInterruptException:
        pass
