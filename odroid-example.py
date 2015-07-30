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

# You should connect ODROID to to Pixhawk's TELEM 1 or TELEM 2 port, 
# not Pixhawk's micro USB. See:
# http://diydrones.com/profiles/blogs/pixhawk-odroid-mavlinkautopylot
#
#PORT = '/dev/ttyACM99' # UART (level-shifter needed: https://www.sparkfun.com/products/12009)
PORT = '/dev/ttyUSB0'   # USB  (FTDI adapter needed: https://store.3drobotics.com/products/ftdi-cable-3-3v)

from mavlink_autopylot import MAVLinkAutoPylot
import time

class AutoPylotTest(MAVLinkAutoPylot):

    def getChannelsPos1(self):

        return [0, 0, 0, 1600] # [roll, pitch, throttle, yaw]

if __name__ == '__main__':

    autopylot = AutoPylotTest(PORT, 57600)

    print('ready')

    while True:

        autopylot.update()

