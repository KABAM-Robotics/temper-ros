#!/usr/bin/env python3 noetic

import rospy
from temper_ros import temper
from sensor_msgs.msg import Temperature


def TEMPerGold_V3():

    pub = rospy.Publisher('/internal_ambient_temperature', Temperature, queue_size=10)
    rospy.init_node('temper', anonymous=True)  
    msg_temp = Temperature()
    msg_temp.header.frame_id = "temperature_sensor_link"
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            msg_temp.header.stamp = rospy.Time.now()
            msg_temp.temperature = float(temper.get_temperature())
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
