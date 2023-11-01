# README #

This README would normally document whatever steps are necessary to get your application up and running.

### Package Description ###

* This ROS package gets internal temperature readings (in degrees Celsius) from PCsensor's TEMPerGold_V3.4 USB thermometer and publishes it to the ROS topic /temp_data
* Version: 1.0
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### Installation ###

* To set up package locally:
    1. Clone into local catkin workspace and build using: catkin_make
  
* To setup USB permissions:
    1. Open terminal and enter: ***sudo vi /usr/lib/udev/rules.d/99-hidraw-permissions.rules***
    2. When vi opens, copy and paste this command into the first line and save the file:
     
		**SUBSYSTEM=="hidraw*", MODE="0666", SYMLINK+="ttyTempSensor"**
        
    3. Exit vi after saving and restart udev using: ***sudo udevadm control --reload***
    4. Open another terminal and enter: **ls -al /dev/hidraw***
    5. Output should show the following:
    <p> crw------- 1 root root    240, 0 May 23 08:43 /dev/hidraw0 <br>
    crw-rw-rw- 1 root root 240, 1 May 23 10:16 /dev/hidraw1 <br>
    crw-rw-rw- 1 root root 240, 2 May 23 10:16 /dev/hidraw2 </p>
	
* Dependencies
    - rospy

### Testing ###

* To test package locally:

    1. Plug in USB thermometer.
    2. Open a terminal and run: roslaunch temper-ros temper_publisher.launch.
    3. Open another terminal and enter: rostopic echo /internal_ambient_temperature.
    5. Data in sensor_msgs/Temperature format should being printing on the rostopic terminal.
    

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

