cmake_minimum_required(VERSION 3.0.2)

project(temper-ros)

##System dependencies
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  sensor_msgs
)

catkin_python_setup()

catkin_package(
LIBRARIES temper-ros
CATKIN_DEPENDS roscpp rospy std_msgs sensor_msgs
)

##Install directives
 catkin_install_python(PROGRAMS
   scripts/temp_pub.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
 )