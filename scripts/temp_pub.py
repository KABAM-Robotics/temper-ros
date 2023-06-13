#!/usr/bin/env python3 noetic

import rospy
from temper_ros import temper
from sensor_msgs.msg import Temperature


def internal_temperature_publisher():

    pub = rospy.Publisher('/internal_ambient_temperature', Temperature, queue_size=10)
    rospy.init_node('internal_temperature_sensor', anonymous=True)  
    msg_temp = Temperature()
    msg_temp.header.frame_id = "internal_temperature_sensor_link"
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        try:
            msg_temp.header.stamp = rospy.Time.now()
            sensor_data = temper.get_temperature()
            msg_temp.temperature = float(sensor_data[0])
            msg_temp.variance = 0
            pub.publish(msg_temp)
            rate.sleep()
        except SystemExit:
            print("Process has exited unexpectedly")

if __name__ == '__main__':
    try:
        internal_temperature_publisher()
    except rospy.ROSInterruptException:
        pass
