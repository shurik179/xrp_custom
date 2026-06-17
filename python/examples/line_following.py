import time
from XRPcustom.defaults import *
   

# LED colors. These can't be used for display colors - those use different format!!
# As usual, each color ranges 0-255, but we suggest using values of 64 or lower - 
# even that is quite bright.
# Blue is dimmer than red and green, so we use higher values 
RED = (32,0,0)
GREEN = (0,32,0)
BLUE = (0,0,64)

display.set_leds(RED)
display.write_line(5,'        Press any button \n               to continue')
display.wait_for_button()
display.clear()
# check taht sensor is connected 
while not linearray.is_connected():
    display.write_line(1, "No sensor found", font=display.largefont, fg=display.RED)
    pass
display.clear()
display.write_line(1, "Sensor found")
linearray.start()
linearray.set_linemode(1) # white line on black background
display.set_leds(GREEN)
display.write_line(3, "Press button B\n to start")
display.wait_for_button()

#speed = 0.3
#Kp = 0.1
speed = 20
Kp = 6
# position of white line 
error = 0
while not linearray.all_black():
    
    #drivetrain.set_effort(speed-Kp*error, speed+Kp*error)
    drivetrain.set_speed(speed-Kp*error, speed+Kp*error)

    # read new position
    pos=linearray.line_pos()
    error = (pos-50)/50 # ranges from -1 (line all the way to the right)
                        # to 1 (line all the way to the left )

drivetrain.stop()
