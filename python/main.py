from machine import Pin
import time
import xrpdisplay
from XRPLib.defaults import *
from XRPLib.pid import PID


def turn2(angle, max_effort = 0.4, timeout = 1.5):
    turn_controller =  PID(
                # kp = 0.2,
                # ki = 0.004,
                # kd = 0.0036,
                kd = 0.003, #scale*(0.0036 + 0.0034 * (max(max_effort, 0.5) - 0.5) * 2),
                kp = 0.03,
                ki = 0.003, # 0.003,
                #kd = 0.007,
                min_output = 0.12,
                max_output = max_effort,
                max_integral = 30,
                tolerance = 1, #degree
                tolerance_count = 3
    )
    drivetrain.turn (angle, timeout = timeout, main_controller = turn_controller)    

def straight2(distance, max_effort = 0.5, timeout = None):
    dist_controller = PID(
        kp = 0.1,
        ki = 0.04,
        kd = 0.04,
        min_output = 0.15,
        max_output = max_effort,
        max_integral = 10,
        tolerance = 0.25,
        tolerance_count = 3,
    )
    
    sync_controller = PID(
        kp = 0.012, kd=0.0005,
    )

    drivetrain.straight(distance, max_effort = max_effort, timeout = timeout,main_controller = dist_controller, secondary_controller = sync_controller)
   

# LED colors. These can't be used for display colors - those use different format!!
# As usual, each color ranges 0-255, but we suggest using values of 64 or lower - 
# even that is quite bright.
# Blue is dimmer than red and green, so we use higher values 
RED = (32,0,0)
GREEN = (0,32,0)
BLUE = (0,0,64)


d = xrpdisplay.XrpDisplay()
# Setting LED colors. First argument is color of left LED, second, of right.
# Second argument is optional; if omitted, same color is used for both LEDs:
# d.set_leds(RED)
d.set_leds(RED, BLUE)
d.write_line(5,'        Press any button \n               to continue')
# buttons. There are 2 buttons, labeled A and B. This command waits
# until a button is pressed, returns button index: 1 for A, 2 for B
d.wait_for_button()
# you can also check if a button is currently pressed:
# if d.is_button_pressed(d.buttonA): 
# basic display usage
d.clear()
d.write_line(3,'Press A to turn left\n   B to turn right')

while True:
    x = d.wait_for_button()
    time.sleep(0.5)    
    if x==1:
        turn2(90)
    else:
        turn2(-90)
        
    
