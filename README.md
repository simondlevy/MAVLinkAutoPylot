# MAVLinkAutoPylot
Python support for autopilot on MAVLink-based flight controllers

A simple way of writing companion-board code for Pixhawk and other MAVLink-based flight controllers. Connects to your FC over a serial port, after which update() method grabs pitch, roll, yaw, and throttle demands that you specify in your subclass.
