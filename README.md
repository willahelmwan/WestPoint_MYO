# usma_myo
ROS package for the myo band

##### Myo band and Robot setup #######
Install ROS, follow the instruction on ROS website. 
Setup MYO band.
1. Google Ros Beginner tutorial
2. Follow 4. Create a ROS Workspace
3. Go to catkin_ws/src , then run this command git clone https://github.com/roboTJ101/ros_myo.git
4. run the command catkin_make in catkin_ws directory
5. run this command in any terminal: echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
6. run this command: sudo usermod -a -G dialout <username>, then logout and log back in.
7. go to /catkin_ws/src/ros_myo/scripts/ , open myo-rawNode.py , change line 300 to typ, val, xdir, _, _, _ = unpack('6B', pay), save and close. 
8. Go to catkin_ws/src, then run this command git clone https://github.com/westpoint-robotics/gvr_bot.git
9. run the command catkin_make in catkin_ws directory
10. navigate to ~/catkin_ws/src/gvr_bot/openjaus/  , run this command tar -xvf openjaus.tar.gz
11. navigate to ~/catkin_ws/src/gvr_bot/scripts/ , run this command chmod 777 run_gvr_bot.sh
12. restart the computer
13. Download the entire folder called GUI_SMI in Robot Setup from the SMI google drive. The username is westpointsmi@gmail.com ,  password is wearable  , Save the GUI_SMI folder in ~/ directory. Navigate to the directory and go into GUI_SMI directory on a terminal and then run the command python Smitass_main.py
14. Go through the tutorial to teach yourself how to use the system. 

Please contact Will Wan if you have any questions at wanwenlin1990@hotmail.com


##### Google Glass note #########
Go to https://github.com/westpoint-robotics/usma_remote_interface
Follow the setup instructions at the bottom.

# Edit the IP address that we want to stream the video
roscd usma_remote_interface/webpage/
gedit config.js

#start the video
roslaunch usma_remote_interface master.launch 
change the ip address to ip 192.168.0.206

Connect all devices to GVR-bot
Go to the IP address on devices that want to see the video by either type in the IP or scan the QR code using the google glass

trouble shooting
Run the setup script.

    $ cd ~/catkin_ws/src/usma_remote_interface/scripts
    $ ./usma_remote_interface_setup.sh


EECSDS3_ROBOTS : accessgranted4robots
GVRBOT WIRELESS PASSWORD: modern0325



