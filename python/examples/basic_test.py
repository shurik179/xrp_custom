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