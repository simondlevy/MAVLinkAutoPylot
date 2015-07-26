#!/usr/bin/env python

'''
MAVLinkAutoPylot ODROID example : cycles throttle or roll for validation.

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

class Cycler(object):

    def __init__(self, chanidx, value, minval, maxval):

        self.chanidx = chanidx
        self.value = value
        self.minval = minval
        self.maxval = maxval
        self.direction = +1

    def cycle(self):

        pwm = [0] * 8
        pwm[self.chanidx] = self.value

        if self.value > self.maxval:
            self.direction = -1

        if self.value < self.minval:
            self.direction = +1

        self.value += self.direction * 10

        return pwm


class AutoPylotTest(MAVLinkAutoPylot):

    def __init__(self, port, baud):

        MAVLinkAutoPylot.__init__(self, port, baud)

        self.throttle = Cycler(2, 1000, 1000, 2000)
        self.roll     = Cycler(0, 1500, 1200, 1800)

    def getChannelsPos1(self):

        return self.throttle.cycle()

    def getChannelsPos2(self):

        return self.roll.cycle()

if __name__ == '__main__':

    autopylot = AutoPylotTest('/dev/ttyACM99', 57600)

    while True:

        autopylot.update()

~                                                                                                                       
~                            
