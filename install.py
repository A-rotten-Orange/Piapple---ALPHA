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


import os
import time 

print "If you are not already you will need to conect to the internet via ethernet"
print "installing please wait"

time.sleep (3)

os.system ("apt-get update")	#Updateing packeges.

time.sleep (3)

os.system ("apt-get install aircrack-ng")	#Installing Aircrack-ng suite.
time.sleep (25)

os.system ("mkdir /piapple-souce")		#Moving ouce files.
os.system ("mv start.py* /piapple-souce")
os.system ("mv dhcp-start.sh* /piapple-souce")
os.system ("mv proberouter.py* /piapple-souce")

print "#######################################"
print "#									 #"
print "#	  start the program with 		 #"
print "#									 #"
print "#'sudo python /piapple-souce/start.py'#"
print "#									 #"
print "#######################################"