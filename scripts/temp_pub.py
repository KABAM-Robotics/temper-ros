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
    prev_temp = 0.0

    while not rospy.is_shutdown():
        try:
            msg_temp.header.stamp = rospy.Time.now()
            sensor_data = temper.get_temperature()
    
            if sensor_data is not None and sensor_data[0] is not None:
                msg_temp.temperature = float(sensor_data[0])
                prev_temp = msg_temp.temperature
            else:
                msg_temp.temperature = prev_temp
                rospy.logerr("Error reading temperature, displaying previously read temperature")
            
            rospy.logdebug(msg_temp)
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
