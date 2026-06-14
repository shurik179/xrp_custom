import time
from XRPcustom.defaults import *


RED = (32,0,0)
GREEN = (0,32,0)

time.sleep(2)
display.clear()
display.set_leds(RED)
display.write_line(1,'Motor test', fg = display.CYAN)
display.write_line(3,'Press any button\n to  run test')
display.write_line(5,'Make sure robot is on \nflat surface, power is on')
display.wait_for_button()
display.set_leds(GREEN)
time.sleep(1)
# Drive forward for 25 cm, 0.8 power
drivetrain.straight(25, 0.8)
time.sleep(1)
drivetrain.turn(90,0.8)
time.sleep(1)
drivetrain.turn(90, -0.8)
time.sleep(1)
drivetrain.straight(-25,0.8)
time.sleep(1)
drivetrain.stop()
display.set_leds(RED)
display.clear()
display.write_line(1, "Test complete", fg=display.GREEN)
