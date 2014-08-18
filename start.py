#Copyright (C) 2014  Harry Sharrock harry@hackapi.org
#               	 @harrysharrock twitter.com
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os
import time

os.system ("cd /piapple-souce") # Change to dir of the program file if you are using a diffrent install dir.

os.system ("sudo airmon-ng start wlan0")
os.system ("sudo ifconfig at0 up") # Change to or wireless adapter of choise e.g mon0 if you are using the aircrack-ng suite.
print "Monitor interface started."
print "mon0 started"
time.sleep(3)

os.system ("sudo sh dhcp-start.sh") # Remove this line if you do not want to use a dhcp server with this program.
os.system ("sudo ifconfig ath0 up")

time.sleep(3)

os.sysytem ("sudo python /piapple-souce/probrouter.py")

time.sleep(5)


