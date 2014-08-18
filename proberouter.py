import os 
import sys
import time

os.system ("airmon-ng start wlan3")
time.sleep(3)

os.system ("airbase-ng -P -Y both mon0")
time.sleep(50)
