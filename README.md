# README #

This README would normally document whatever steps are necessary to get your application up and running.

### Package Description ###

* This ROS package gets internal temperature readings (in degrees Celsius) from PCsensor's TEMPerGold_V3.4 USB thermometer and publishes it to the ROS topic /temp_data
* Version: 1.0
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### Installation ###

* To set up package locally:
  - clone into local catkin workspace and build using: catkin_make
  
* To setup USB permissions:
  - open terminal and enter: sudo vi /etc/udev/rules.d/99-hidraw-permissions.rules
  - when vi opens, copy and paste this command into the first line and save the file:
  
    KERNEL=="hidraw*", SUBSYSTEM=="hidraw", MODE="0664", GROUP="plugdev"

  - exit vi after saving and restart udev using: sudo udevadm control --reload
  - to check if the permissions have been set, open another terminal and enter: ls -al /dev/hidraw*
  -the output should show the following:
	
	crw------- 1 root root    240, 0 May 23 08:43 /dev/hidraw0
	crw-rw-r-- 1 root plugdev 240, 1 May 23 10:16 /dev/hidraw1
	crw-rw-r-- 1 root plugdev 240, 2 May 23 10:16 /dev/hidraw2
	
* Dependencies
  - rospy

### Testing ###

* To test package locally:
  - plug in USB thermometer
  - open a terminal and start roscore
  - open another terminal and enter: rosrun temper-ros temp_pub.py
  - open another terminal and enter: rostopic echo /temp_data
  - data should being printing on the rostopic terminal

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines
