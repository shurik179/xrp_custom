

.. _imu:

Inertial Motion Unit
====================

This section describes the functions for using the built-in Inertial Motion
Unit (IMU).

XRP contains a built-in Inertial Motion Unit (IMU), which combines a 3-axis accelerometer and a
3-axis gyro sensor, providing information about acceleration and rotational
speed. 
XRP firmware combines the sensor data to provide information
about robot's orientation in space, in the form of Yaw, Pitch, and Roll angles.

Below is a breif  description of some functions related to IMU. Detailed information about the 
IMU and its use can be found in official 
 `API reference <https://open-stem.github.io/XRP_MicroPython/api.html#XRPLib.imu.IMU>`__. 

All methods below are methods of the `imu` object, so they should be called as `imu.get_heading()`, `imu.get_yaw()`, etc.



.. function:: get_heading()

   The heading (yaw) of the IMU in degrees, bound between [0, 360)

.. function:: get_yaw()

    Get the yaw (heading) of the IMU in degrees. Unbounded in range. 
    This can be useful for tracking the total rotation of the robot, 
    for example, if you want to turn by more than 360 degrees. 

.. function:: reset_yaw()

    Resets the yaw (heading) of the IMU to 0.

.. function:: calibrate(calibration_time: float = 1)

    Calibrate the IMU; this helps to improve the accuracy of the IMU readings. This function 
    collects readings for [calibration_time] seconds and calibrates the IMU based on those readings 
    (5 seconds is recommended time). Do not move the robot during this time. Assumes the board to be parallel to the ground. 