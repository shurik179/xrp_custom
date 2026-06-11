Driving
=======

Of course, main use of this robot is to drive around, and for this, we need to
control the motors.

XRP has two drive motors, each equipped with an encoder (rotation counter). This allows us to control the motors in a closed loop, using feedback from the encoders to maintain desired speed or to drive a specific distance.

Detailed information about driving the robot can be found in official 
XRP documentation (`User guide  <https://xrpusersguide.readthedocs.io/en/latest/course/driving.html>`__,
`API reference <https://open-stem.github.io/XRP_MicroPython/api.html#XRPLib.differential_drive.DifferentialDrive>`__);  
here we will give a brief overview of the most commonly used commands.  

All of the commands below are methods of the `drivetrain` object, so they should be called as `drivetrain.straight(...)`, `drivetrain.turn(...)`, etc.

.. function:: stop()

   Stops the robot by setting the power to both motors to 0. 

.. function:: set_effort(left_effort: float, right_effort: float)

   Sets the effort (power) of the left and right motors; effort is measured as a fraction of the maximum effort.
   This function does not use encoders; because of that and individual variations in motor efficiency, even if power of both motors is the same, 
   the robot may not drive straight, and the actual speed may be different from what you expect.
  

.. function:: set_speed(left_speed: float, right_speed: float)

   Sets the speed of the left and right motors; speed is measured in centimeters per second. This function uses encoder feedback to maintain the desired speed.
  
 
.. function:: straight(distance, effort=0.5)

   Move forward/backward  by given distance (in centimeters) at given effort (i.e. 
   power level). Effort should be from -1 (reverse at full speed) to 1 (forward at full speed). 
   It is optional; if not given, the default effort of 0.5 (i.e. half of maximal) is used.

   This command uses encoder readings to determine how far to drive, and tries to keep the robot on straight path by using IMU. 

   This command has a number of optional paramеters not documented here, see `API reference <https://open-stem.github.io/XRP_MicroPython/api.html#XRPLib.differential_drive.DifferentialDrive>`__ for details.

.. function:: turn(angle, effort=0.5)

   Turn by given angle, in degrees. Positive values correspond to turning right (clockwise).
   Parameter ``effort`` is  optional; if not given, default effort  of 0.5 (i.e. half of maximal) is used.


Encoders
--------
You can check encoders (rotation counters) of the motors so that you can see how far the robot has actually travelled. 

.. function:: get_left_encoder_position()

.. function:: get_right_encoder_position()

   Returns the current position of the left/right motor’s encoder in cm.


.. function:: reset_encoder_position()

   Resets the position of both motors’ encoders to 0

