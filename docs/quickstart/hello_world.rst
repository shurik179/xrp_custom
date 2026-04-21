First program
=============

To create your first program, start Thonny. Create a new file (using `File->New` menu item)
and copy-paste in the file the following lines:


.. code-block:: python

  import time
  from XRPcustom.defaults import *


  RED = (32,0,0)
  GREEN = (0,32,0)

  time.sleep(2)
  display.clear()
  display.set_leds(RED, GREEN)
  display.write_line(3,' Press  button A \n  to switch colors')
  while True:
    if display.is_button_pressed(display.buttonA):
        display.set_leds(RED, GREEN)
    else:
        display.set_leds(GREEN, RED)


This program is mostly self-explanatory. Command `time.sleep(2)` causes the robot to pause for 2 seconds; 
`display.clear()` clears the display, and `display.set_leds(RED, GREEN)` sets the color of the left and right LEDs. The colors are defined as a triple of values (RGB), each number ranging 0-255. 
The value we used (32) is bright enough to be visible but not so bright that it hurts your eyes. 
The command `display.write_line(3,' Press  button A \n  to switch colors')` writes the text on the display; `\n` is a 
special symbol that causes the text to be written on a new line. Function `display.is_button_pressed(display.buttonA)` checks if button A is pressed.

Now, use `File->save as` menu item to save this file. When prompted, choose
`RP2040 device` and enter file name `main.py` (this is important!).

Click green arrow at the top of Thonny window to run this file now. 

You can disconnect the robot from the computer and restart it by turning it off
and on. Upon restart, it will automatically run the code in `main.py`.

You can now experiment with the program, modifying it any way you like. Here
are some useful tips:

* You can have many programs uploaded to the robot, but by default, upon restart
  it will execute file with name `main.py`. Thus, it makes sense to always use
  this file for your program.

* If your program is running, or if you disconnected and reconnected your robot
  to the computer, you need to hit `STOP` icon to stop the program before you
  can save a new version of the program

* If you have difficulty connecting to the robot, try turning off the robot power switch before connecting it to computer. 
  (USB cable provides enough power for the microcontroller to run, but it may not be enough to power the motors.)
  
* when copying and pasting, make sure that the  indentation is correct!

* When ending your work session, it is highly recommended to save a copy of the
  program to the computer!
