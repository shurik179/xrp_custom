from machine import Pin, SPI
import time
import xrpdisplay

RED = (64,0,0)
GREEN = (0,24,0)
BLUE = (0,0,32)

d = xrpdisplay.XrpDisplay();

d.set_leds(GREEN, BLUE)