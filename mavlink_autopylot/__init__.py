'''
mavlink_autopylot - Python support for autopilot on MAVLink-based flight controllers

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

from pymavlink import mavutil

class MAVLinkAutoPylot(object):

    def __init__(self, port, baud, sendrate=10, pos1usec=1000, pos2usec=1600):
        '''
        Creates a connection to a MAVLink flight controller over the specified serial port at the 
        specified baud rate.  Optional sendrate specifies data-streaming reate in Hz, pos1usec specfies
        PWM value for detecting switch in position 1, pos2usec for position 2.
        '''

        self.mavmaster = mavutil.mavlink_connection(port, baud)

        self.pos1usec = pos1usec
        self.pos2usec = pos2usec
   
        self.ready = False

        self.default_values = [0] * 8

        # wait for the heartbeat msg to find the system ID
        self.mavmaster.wait_heartbeat()

        # request data to be sent at the given rate
        self.mavmaster.mav.request_data_stream_send(self.mavmaster.target_system, self.mavmaster.target_component, 
            mavutil.mavlink.MAV_DATA_STREAM_ALL, sendrate, 1)

    def update(self):
        '''
        Updates the autopilot.  Call this method in a loop.
        If channel 5 is in position 1, R/C channel values are set to the values returned
        by getChannelsPos1(); if position 2, to values returned from getChannelsPos2().  Otherwise, receiver
        values are used.
        '''

        msg = self.mavmaster.recv_match(blocking=False)

        if msg != None:

            if msg.get_type() == 'RC_CHANNELS_RAW':

                if self.ready:

                    if msg.chan5_raw > self.pos2usec:
                        self._send_rc(self.getChannelsPos2())

                    elif msg.chan5_raw > self.pos1usec:
                        self._send_rc(self.getChannelsPos1())

                    else:
                        self._send_rc([0] * 4)

                elif msg.chan5_raw < self.pos1usec:
                    self.ready = True

    # attempt to send a control
    def _send_rc(self, data):


        self.mavmaster.mav.rc_channels_override_send(self.mavmaster.target_system, 
                self.mavmaster.target_component, *(data+[0]*4))

    def getChannelsPos1(self):
        '''
        This method is automatically called when the channe 5 switch is in position 1.
        Default behavior is returning all zeros, so that the original receiver values are used.
        Override for your application, returning desired [roll, pitch, yaw, throttle] list.
        '''
        return [0] * 4

    def getChannelsPos2(self):
        '''
        This method is automatically called when the channe 5 switch is in position 2.
        Default behavior is returning all zeros, so that the original receiver values are used.
        Override for your application, returning desired [roll, pitch, yaw, throttle] list.
        '''
        return [0] * 4
