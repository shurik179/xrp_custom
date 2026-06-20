
import time
from XRPcustom.defaults import *

# check that sensor is connected 
if not linearray.is_connected():
    print("Connection failure")
    display.write_line(5, "No sensor found", font=display.largefont, fg=display.RED)
    while True:
        pass

###################################################
display.clear()
display.write_line(1,'Reflectance array', fg = display.CYAN)

linearray.start()
linearray.set_linemode(1) #white line on black background
fw_version = linearray.fw_version()
display.write_line(1, "Firmware: {}".format(fw_version))
display.write_line(4,'Press A to calibrate\n   B to skip calibration')
x = display.wait_for_button()
display.clear()
if x==1:
    # calibrate
    display.write_line(1, "Calibrating...")
    display.write_line(2, "Move robot around \n over black and white")
    display.write_line(4, "Press A to finish")
    linearray.start_cal() 
    display.wait_for_button()
    linearray.end_cal()
    display.clear()
    display.write_line(1, "Calibration complete", fg=display.GREEN) 
    time.sleep(2)
# main loop - just print values
display.write_line(1, "Press A to stop")
display.write_line(2, "Cal. values (0-100)")
display.write_line(4, "Line position (0-100):")

values = [0,0,0,0,0,0]
while not display.is_button_pressed(display.buttonA):
    for s in range(6):
        value = linearray.calibrated(s)
        values[s]=((int)(value/10.23)) #convert to percentage, so range 0-1023 becomes 0-100
    display.write_line(3, ' '.join(f'{v:3}' for v in values), fg=display.BLUE)
    pos = linearray.line_pos()
    display.write_line(5, f'               {pos:3}', fg=display.BLUE)
    time.sleep(0.3)
