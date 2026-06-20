Reflectance sensor array
========================
Our version of XRP uses a custom reflectance sensor array, containing 6 reflectance sensors 
(as opposed to 2 sensors in the stock version). This sensor is fully documented in a separate 
github repository, `Reflectance Sensor Array <hhttps://github.com/shurik179/reflectance_array>`_.

This sensor  has a built-in array of reflectance sensors, pointed down. These sensors
can be used for detecting field borders, for following the line, and other similar
tasks.

All methods described below are methods of the `linearray`  object, so they should be called as `linearray.start()`, etc. 
Sensor index ``s`` ranges between 0--5; 0 is the rightmost sensor, and 5, the leftmost.

Basic commands
---------------

.. function:: start()
.. function:: stop() 

    Starting and stopping the sensor. By default, the sensor is active. To save battery, 
    you can stop it by using `stop()`; this turns off the power to IR LEDs inside reflectance 
    sensors.  Note that you can still read the reflectance sensor values even when the LEDs are off; 
    this can be useful for detecting ambient light changes.


.. function:: is_connected()

   Returns ``True`` if the reflectance sensor array is connected and ``False`` otherwise.
   It is a good practice to check that the sensor is connected before using it.     

.. function:: fw_version()

    Returns firmware version as a string, e.g. `1.3`

.. function:: raw(s)

   Returns raw reading of  s-th reflection sensor (0-1023). The darker the surface, 
   the lower the value. Typical value on a white sheet of paper is around 950, 
   and on black plastic, around 120. 


Calibration
===========
You can calibrate the sensor, recording  values for black and white; these values 
will be used for computing calibrated readings and for deciding when the sensor 
is on black/white (see below). 

 The calibration values are saved in persistent memory of the sensor, 
 which means that they are preserved  even when you turn off the  power to the sensor; 
 they  will be loaded on next power-up. 



.. function:: start_cal()
.. function:: end_cal()

   Starts and stops calibration. In between these commands, it is expected that 
   you move the robot (without lifting it!) so that each sensor sees both white and black. The lowest 
   recorded value will be saved as black calibration, and the highest, as white 
   calibration; these are saved individaully per sensor.

.. function:: get_cal_black(s)
.. function:: get_cal_white(s)

   Returns the value of black (respectively, white) calibration for sensor s. 
   This is rarely needed - mostly to verify that calibration was successful 
   in cases when your sensor behaves unexpectedly. 
   

Calibrated readings
===================
.. function:: calibrated(s)

   This function assumes that you had already calibrated your sensor. It returns 
   calibrated value. For example, if calibration values were 300 (black) and 800 (white)
   then raw reading of 300 or less  will give calibrated reading 0, raw reading of 800 
   or above will give calibrated reading of 1023, and all values in between will be 
   rescaled linearly - e.g., raw reading of 550 (which is exactly the midpoint between 300 and 800)
   will give calibrated reading of 512. 

Digital readings
================  
In many cases you only need to know if the sensor is on black/white and not interested in exact reading. 
In these cases, it is much faster to use the functions below. As before, you should calibrate 
your sensor before using these functiosn. 

.. function:: on_black(s)
.. function:: on_white(s)

   Returns True if sensor s is on black (respectively, white) and False otherwise. 
   The cutoff between white and black is defined to be the  midpoint between black 
   and white calibration values. 

.. function:: all_black()
.. function:: all_white()

   Returns True if all sensors are on black (respectively, white) and False otherwise. 


Line position 
=============

For line following tasks, you can use the functions below. They work best with line widths of 1/2-3/4" 
(12-20mm). 

.. function:: set_linemode(mode)

   Sets the mode for line position function. There are two possible modes: 
   
   0 - for black line on white background

   1 - for tracking white line on black background 
   
   
.. function:: line_pos()

   Returns the position of the line under the robot. The return  value ranges 0-100; 
   0 means that the line is all the way to the right and 100, all the way to the left. 
   If no sensor sees the line, the function will still return a value, which is unpredictable. 



