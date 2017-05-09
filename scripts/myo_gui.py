#!/usr/bin/python
import os
#http://stackoverflow.com/questions/3730964/python-script-execute-commands-in-terminal
import time
#http://www.cyberciti.biz/faq/python-sleep-command-syntax-example/
#Spawn new terminal http://askubuntu.com/questions/46627/how-can-i-make-a-script-that-opens-terminal-windows-and-executes-commands-in-the
#Kill all Xterm http://stackoverflow.com/questions/3881489/kill-all-processes-launched-inside-an-xterm-when-exit
os.system("killall -9 roscore")
os.system("killall -9 rosmaster")
os.system("killall xterm")
os.system("xterm -e roscore &")
time.sleep(5)
os.system("xterm -e rosrun ros_myo myo-rawNode.py &")
time.sleep(5)
os.system("xterm -e rosrun gvr_bot run_gvr_bot.sh &")
time.sleep(5)
os.system("xterm -e rosrun MYO myo_v2.py")



