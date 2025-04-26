# SPDX-FileCopyrightText: Copyright 2025 Alexander Kirillov <shurik179@gmail.com>
#
# SPDX-License-Identifier: MIT

"""
`xrp display`
====================================================

This is a micropython library for XRP display by Alexander Kirillov.

* Author(s): Alexander Kirillov
* Version: 1.0
"""

# import micropython libraries 
from machine import Pin, SPI
import time
import sys
import neopixel
# For SPI display
import st7789py as st7789
import vga1_bold_16x32
disp_sck  = 18 # default SCK of SPI(0)
disp_mosi = 19 # default MOSI of SPI(0)
disp_miso = 16  # not use
disp_res = 14
disp_dc  = 15
disp_cs  = 17
DISP_WIDTH = 135
DISP_HEIGHT = 240

class XrpDisplay:
    def __init__(self, neopixel_pin=37):
        self.npxl = neopixel.NeoPixel(Pin(neopixel_pin, Pin.OUT), 3)
        self.brightness = 64
        disp_spi = SPI(0,  sck=Pin(disp_sck), mosi=Pin(disp_mosi), miso=None)
        #print(disp_spi)

        self.display = st7789.ST7789(disp_spi,
                        DISP_WIDTH, DISP_HEIGHT,
                        rotation = 3,
                        reset=Pin(disp_res, Pin.OUT),
                        cs=Pin(disp_cs, Pin.OUT),
                        dc=Pin(disp_dc, Pin.OUT),
                        backlight=None)
        # print(st7789.__name__, display.width, "x", display.height)
        self.display.fill(st7789.WHITE)
        self.display.fill_rect(1, 1, self.display.width-2, self.display.height-2, st7789.BLACK)
        
        self.display.text(font = vga1_bold_16x32,
             text = "Welcome to",
             x0 = 40,
             y0 = 20,
             color = st7789.RED,
             background = st7789.BLACK)

        self.display.text(font = vga1_bold_16x32,
             text = "XRP",
             x0 = 80,
             y0 = 60,
             color = st7789.RED,
             background = st7789.BLACK)

    def set_leds(self, left_color, right_color = None):
        if right_color is None:
            right_color = left_color
        self.npxl[1]=left_color
        self.npxl[2]=right_color
        self.npxl.write()

        