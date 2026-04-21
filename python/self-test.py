import time
from XRPcustom.defaults import *
   

# LED colors. These can't be used for display colors - those use different format!!
# As usual, each color ranges 0-255, but we suggest using values of 64 or lower - 
# even that is quite bright.
# Blue is dimmer than red and green, so we use higher values 
RED = (32,0,0)
GREEN = (0,32,0)
BLUE = (0,0,64)



# Print welcome message
print("------------------------------------------")
print("Running Self-Test Program!")
print("------------------------------------------")

# Setting LED colors. First argument is color of left LED, second, of right.
# Second argument is optional; if omitted, same color is used for both LEDs:
# d.set_leds(RED)
display.set_leds(RED, BLUE)
display.write_line(5,'        Press any button \n               to continue')
# buttons. There are 2 buttons, labeled A and B. This command waits
# until a button is pressed, returns button index: 1 for A, 2 for B
display.wait_for_button()
# you can also check if a button is currently pressed:
# if d.is_button_pressed(d.buttonA): 
display.clear()
display.set_leds(GREEN)
###################################################
print("Testing reflectance sensor")
display.write_line(1,'Reflectance array test', fg = display.CYAN)
display.write_line(3,'Press A to run test\n   B to skip')
x = display.wait_for_button()
display.clear()
if x==1:
    display.write_line(5,'Press A to continue')
    if linearray.is_connected():
        linearray.start()
        fw_version = linearray.fw_version()
        print("Linearray firmware version: {}".format(fw_version))
        display.write_line(1, "Firmware: {}".format(fw_version))
        values = [0,0,0,0,0,0]
        while not display.is_button_pressed(display.buttonA):
            for s in range(6):
                value = linearray.raw(s)
                values[s]=((int)(value/10.23)) #convert to percentage
                # formatted to take 4 characters, for better alignment
                print(f'{value:4}', end=' ')
            print('') #just to end the line
            display.write_line(2, "Values (percentage)",  font=display.smallfont2)
            display.write_line(3, ' '.join(f'{v:3}' for v in values))
            time.sleep(0.3)
    else:
        display.write_line(2, "No sensor found", font=display.largefont, fg=display.RED)
        time.sleep(3)
    
else:
    print("Linearray test skipped")
    display.write_line(1, "Linearray test skipped")
    time.sleep(1)
    
display.clear()
time.sleep(0.5)
###################################################
print("Testing distance sensor")
display.write_line(1,'Distance sensor test', fg = display.CYAN)
display.write_line(3,'Press A to run test\n   B to skip')
x = display.wait_for_button()
display.clear()
if x==1:
    display.write_line(5,'Press A to continue')
    while not display.is_button_pressed(display.buttonA):
        dist = rangefinder.distance()
        print(f"Range    Distance: {dist:.1f}    Press user button to test servo")
        time.sleep(0.1)
        display.write_line(1,f"Dist: {dist:.1f}", font=display.largefont)

else:
    print("Distance test skipped")
    display.write_line(1, "Distance test skipped")
    time.sleep(1)
    
display.clear()
time.sleep(0.5)
###################################################
# Test servo
print("Testing servo")
display.write_line(1,'Servo test', fg = display.CYAN)
display.write_line(3,'Press A to run test\n   B to skip')
x = display.wait_for_button()
if x==1:
    time.sleep(1)
    servo_one.set_angle(90)
    time.sleep(1)
    servo_one.set_angle(0)
    time.sleep(1)
    servo_one.set_angle(180)
else:
    print("Servo test skipped")
    display.clear()
    display.write_line(1, "Servo test skipped")
    time.sleep(1)
    
display.clear()   
time.sleep(0.5)
###################################################
# Print warning and wait for button press
print()
print("The next test will drive the motors, so place the robot on a flat surface!")
print("Also please make sure the power switch is turned on!")
print("Press user button to test drivetrain")
display.write_line(1,'Motor test', fg = display.CYAN)
display.write_line(3,'Press A to run test\n   B to skip')
display.write_line(5,'Make sure robot is on \nflat surface, power is on')
x = display.wait_for_button()
if x==1:
    print("Testing drivetrain")
    time.sleep(1)
    drivetrain.straight(25, 0.8)
    time.sleep(1)
    drivetrain.turn(90,0.8)
    time.sleep(1)
    drivetrain.turn(90, -0.8)
    time.sleep(1)
    drivetrain.straight(-25,0.8)
else:
    print("Motor test skipped")
    display.clear()
    display.write_line(1, "Motor test skipped")
    time.sleep(1)
display.clear()
###################################################
print()
print("-----------------------------------")
print("All tests complete! Happy roboting!")
print("-----------------------------------")

display.write_line(2,'All tests complete!', fg = display.GREEN, font = display.largefont)
display.write_line(4,'Happy roboting!', fg = display.GREEN,font = display.largefont)