# Do not skip line 2
#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from temper_ros.temper import main

data = '0'

def TEMPerGold_V3():
    global data

    pub = rospy.Publisher('/temp_data', String, queue_size=10)
    rospy.init_node('TEMPer', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            data = main()
        except SystemExit:
            print("Process has exited unexpectedly")
        finally:
            pub.publish(data)
            rate.sleep()

if __name__ == '__main__':
    try:
        TEMPerGold_V3()
    except rospy.ROSInterruptException:
        pass
