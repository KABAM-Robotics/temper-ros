# Do not skip line 2
#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Temperature
from temper_ros.temper import main

data = '0'

def TEMPerGold_V3():
    global data

    pub = rospy.Publisher('/temp_data', Temperature, queue_size=10)
    rospy.init_node('TEMPer', anonymous=True)  
    msg_temp = Temperature()
    msg_temp.header.frame_id = "TEMPer"
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            now = rospy.get_rostime()
            msg_temp.header.stamp.secs = now.secs
            msg_temp.header.stamp.nsecs = now.nsecs
            msg_temp.temperature = float(main())
            msg_temp.variance = 0
            pub.publish(msg_temp)
            rate.sleep()
        except SystemExit:
            print("Process has exited unexpectedly")

if __name__ == '__main__':
    try:
        TEMPerGold_V3()
    except rospy.ROSInterruptException:
        pass
