from XRPLib.board import Board
from machine import Timer, Pin
from neopixel import *
import time
board = Board.get_default_board()
npxl_pin= Pin(37, Pin.OUT)
my_rgb=NeoPixel(npxl_pin, 3)

my_rgb[1]=(64,0,0)
my_rgb[2]=(0,0,64)
my_rgb.write()
