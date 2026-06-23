Cheat sheet
====================================


Initialization
---------------

.. code-block:: python

   import time
   from XRPcustom.defaults import *

Time control
------------
.. function:: time.delay(t)

   Wait for `t` seconds 

Display
-------

.. function:: display.clear()

   Blank the display

.. function:: display.write_line(i, text)

   Print message on i-th line

.. function:: display.set_leds(color_l, color_r)

.. function:: display.wait_for_button()

   Waits until the user presses any button

.. function:: display.is_button_pressed(button)

   Returns ``True`` if given button is currently pressed and ``False`` otherwise.

Drivetrain
----------


.. function:: drivetrain.stop()

   Stops the robot by setting the power to both motors to 0. 
  

.. function:: drivetrain.set_speed(left_speed, right_speed)

   Sets the speed of the left and right motors; speed is measured in centimeters per second (15 cm/sec is reasonable speed)
 
.. function:: drivetrain.straight(distance, effort=0.5)

   Move forward/backward  by given distance (in centimeters) at given effort (i.e. 
   power level, ranges 0-1).

.. function:: drivetrain.turn(angle, effort=0.5)

   Turn by given angle, in degrees. Positive values of angle correspond to turning left (counterclockwise); 
   negative, to turning right. 


Linearray sensor
-----------------
.. function:: linearray.start()


.. function:: linearray.on_black(s)
.. function:: linearray.on_white(s)

   Returns True if sensor s is on black (respectively, white) and False otherwise.
   s ranges from 0 (rightmost) to 5 (leftmost) 

.. function:: linearrya.all_black()
.. function:: linearray.all_white()



.. function:: linearray.set_linemode(mode)

   Sets the mode for line position function. There are two possible modes: 
   
   0 - for black line on white background

   1 - for tracking white line on black background 
   
   
.. function:: linearray.line_pos()

   Returns the position of the line under the robot. The return  value ranges 0-100; 
   0 means that the line is all the way to the right and 100, all the way to the left. 
   If no sensor sees the line, the function will still return a value, which is unpredictable. 
