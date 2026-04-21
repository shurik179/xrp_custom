Initialization and general functions
====================================

To begin using the library, you need to put the following in the beginning of
your `main.py` file:

.. code-block:: python

   import time
   from XRPcustom.linearray import *



This creates several objects that you will be using to control the robot:
*  `display` - object representing the OLED display with LEDs and buttons
*  `drivetrain` - object representing the drivetrain (drive motors and encoders)
*  `linearray`` - object representing the reflectance line array sensor, used for detecting the line on the floor
*  `rangefinder` - object representing the distance sensor, used for detecting obstacles in front of the robot
*  `imu` - object representing the inertial measurement unit, used for detecting the robot's orientation and acceleration
*  `servo_one` and `servo_two` - objects representing the two servo motors (if you have them connected)


