"""
Raspberry Pi Pico/MicroPython exercise
to display on 1.54" IPS 240x240 with SPI ST7789 driver

Hello World and color test

Using library: russhughes/st7789py_mpy,
driver for 320x240, 240x240, 135x240 and 128x128 ST7789 displays written in MicroPython.
(https://github.com/russhughes/st7789py_mpy)

Connection:
-----------
GND   GND
VCC           3V3
SCL           GP18
SDA (MOSI)    GP19
RES           GP14
DC            GP15
CS            GP17
BLK           3V3
      GP16 (dummy, not used)
"""

import os, sys
from machine import Pin, SPI
import time
import st7789py as st7789
import vga1_bold_16x32
# more fonts here: https://github.com/russhughes/st7789py_mpy/tree/master/romfonts

disp_sck  = 18 # default SCK of SPI(0)
disp_mosi = 19 # default MOSI of SPI(0)
disp_miso = 16  # not use
disp_res = 14
disp_dc  = 15
disp_cs  = 17
disp_blk = 22

print("====================================")
print(sys.implementation[0], os.uname()[3],
      "\nrun on", os.uname()[4])
print("====================================")

DISP_WIDTH = 135
DISP_HEIGHT = 240

# it's found that:
# - cannot set baudrate
# - even I set miso=None, miso will be assigned deault GP16 or previous assigned miso
disp_spi = SPI(0,  sck=Pin(disp_sck), mosi=Pin(disp_mosi), miso=None)
print(disp_spi)

display = st7789.ST7789(disp_spi,
                        DISP_WIDTH, DISP_HEIGHT,
                        rotation = 3,
                        reset=Pin(disp_res, Pin.OUT),
                        cs=Pin(disp_cs, Pin.OUT),
                        dc=Pin(disp_dc, Pin.OUT),
                        backlight=None)
print(st7789.__name__, display.width, "x", display.height)

display.fill(st7789.WHITE)
display.fill_rect(1, 1, display.width-2, display.height-2, st7789.BLACK)

display.text(font = vga1_bold_16x32,
             text = "Hello",
             x0 = 10,
             y0 = 10,
             color = st7789.WHITE,
             background = st7789.BLACK)
display.text(vga1_bold_16x32,
             st7789.__name__,
             10,
             42,
             st7789.WHITE,
             st7789.BLACK)

# display title on last line, center horizontally.
# for 16x32 font
title_text = "shurik179"
display.text(vga1_bold_16x32,
             title_text,
             int((display.width - len(title_text)*16)/2),  # center horizontally
             display.height - 32,             # last line
             st7789.GREEN,
             st7789.BLACK)
time.sleep(5)
#color test
color_factor = 255/(240+240)
   
print("RED:\t", end="")
start_time = time.ticks_ms()
for y in range(display.height):
    for x in range(display.width):
        r = int((x + y) * color_factor)
        display.pixel(x, y, st7789.color565(r, 0, 0))
end_time = time.ticks_ms()
print("ticks_diff()", time.ticks_diff(end_time, start_time), "ms")
        
print("GREEN:\t", end="")
start_time = time.ticks_ms()
for y in range(display.height):
    for x in range(display.width):
        g = int((x + y) * color_factor)
        display.pixel(x, y, st7789.color565(0, g, 0))
end_time = time.ticks_ms()
print("ticks_diff()", time.ticks_diff(end_time, start_time), "ms")

print("BLUE:\t", end="")
start_time = time.ticks_ms()
for y in range(display.height):
    for x in range(display.width):
        b = int((x + y) * color_factor)
        display.pixel(x, y, st7789.color565(0, 0, b))
end_time = time.ticks_ms()
print("ticks_diff()", time.ticks_diff(end_time, start_time), "ms")

print("WHITE:\t", end="")
start_time = time.ticks_ms()
for y in range(display.height):
    for x in range(display.width):
        w = int((x + y) * color_factor)
        display.pixel(x, y, st7789.color565(w, w, w))
end_time = time.ticks_ms()
print("ticks_diff()", time.ticks_diff(end_time, start_time), "ms")

print("~ bye ~")
