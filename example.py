#!/usr/bin/env python

'''
MAVLinkAutoPylot example : cycles throttle or roll for validation.

Copyright (C) Simon D. Levy 2015

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

class AutoPylotTest(MAVLinkAutoPylot):

    def __init__(self, port, baud):

        MAVLinkAutoPylot.__init__(self, port, baud)

        self.throttle = 1000
        self.throttledir = +1

        self.roll = 1500
        self.rolldir = +1

    def getChannelsPos1(self):

        pwm = [0] * 8
        pwm[2] = self.throttle

        if self.throttle > 2000:
            self.throttledir = -1

        if self.throttle < 1000:
            self.throttledir = +1

        self.throttle += self.throttledir * 10

        return pwm

    def getChannelsPos2(self):

        pwm = [0] * 8
        pwm[0] = self.roll

        if self.roll > 1800:
            self.rolldir = -1

        if self.roll < 1200:
            self.rolldir = +1

        self.roll += self.rolldir * 10

        return pwm


if __name__ == '__main__':

    autopylot = AutoPylotTest('/dev/ttyUSB0', 57600)

    print('Connected ... hit CTRL-C to quit')

    while True:

        try:

            autopylot.update()

        except KeyboardInterrupt:

            break

