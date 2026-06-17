import time
from XRPcustom.defaults import *


# check that sensor is connected 
if not linearray.is_connected():
    print("Connection failure")
    display.write_line(5, "No sensor found", font=display.largefont, fg=display.RED)
    while True:
        pass

RED = (32,0,0)
GREEN = (0,32,0)

###################################################
display.clear()
display.write_line(1,'stay within lines', fg = display.CYAN)

linearray.start()
linearray.set_linemode(1)
display.write_line(4,'Press A to continue')
display.wait_for_button()


while True:
    display.set_leds(GREEN)
    drivetrain.set_speed(15,15)
    while linearray.all_black():
        pass
    #if we are here, it means at least one of sensors sees white
    drivetrain.stop()
    display.set_leds(RED)
    if linearray.on_white(0) or linearray.on_white(1): #one of right sensor sees white; turn left
        drivetrain.turn(120, 0.4)
    else:
        drivetrain.turn(-120,0.4)
