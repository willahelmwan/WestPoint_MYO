#!/usr/bin/python
import os
import time
os.system("env")
#os.system("(env; export PYTHONPATH=/home/smi/catkin_ws/devel/lib/python2.7/dist-packages:/opt/ros/indigo/lib/python2.7/dist-packages; export PATH=$PATH:/opt/ros/indigo/bin/; export ROS_MASTER_URI='http://localhost:11311';roscore)")
#os.system("$HOME/catkin_ws/src/MYO/scripts/test.sh")
os.system("xterm -hold -e roscore")
time.sleep(1000)

