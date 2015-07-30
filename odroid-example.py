#!/usr/bin/env python

'''
MAVLinkAutoPylot ODROID example : yaws right gently, for validation.

Copyright (C) Simon D. Levy 2015

To use this script, you must install pymavlink as root (not sudo!)
I followed the directions here: https://pixhawk.org/dev/pymavlink.
Then put the following line in /etc/rc.local:

python /home/odroid/MAVLinkAutoPylot/odroid-example.py

This code is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as 
published by the Free Software Foundation, either version 3 of the 
License, or (at your option) any later version.
This code is distributed in the hope that it will be useful,     
but WITHOUT ANY WARRANTY without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU Lesser General Public License 
along with this code.  If not, see <http:#www.gnu.org/licenses/>.
'''

from mavlink_autopylot import MAVLinkAutoPylot
import time

class AutoPylotTest(MAVLinkAutoPylot):

    def getChannelsPos1(self):

        return self.throttle.cycle()

if __name__ == '__main__':

    autopylot = AutoPylotTest('/dev/ttyACM99', 57600)

    while True:

        autopylot.update()

~                                                                                                                       
~                            
