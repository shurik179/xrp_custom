from XRPLib.board import Board
# note: this is where se are using our own drivetrain, not XRPLib one 
from .differential_drive import DifferentialDrive 
from XRPLib.motor import SinglePWMMotor, DualPWMMotor
from XRPLib.encoder import Encoder
from XRPLib.encoded_motor import EncodedMotor
from XRPLib.rangefinder import Rangefinder
from XRPLib.imu import IMU
from XRPLib.reflectance import Reflectance
from XRPLib.servo import Servo
from XRPLib.webserver import Webserver
from .xrpdisplay import XrpDisplay
from .linearray import LineArray
from machine import Pin, I2C

"""
A simple file that constructs all of the default objects for the XRP robot
Run "from XRPcustom.defaults import *" to use
"""

left_motor = EncodedMotor.get_default_encoded_motor(index=1)
right_motor = EncodedMotor.get_default_encoded_motor(index=2)
motor_three = EncodedMotor.get_default_encoded_motor(index=3)
motor_four = EncodedMotor.get_default_encoded_motor(index=4)
imu = IMU.get_default_imu()
drivetrain = DifferentialDrive.get_default_differential_drive()
rangefinder = Rangefinder.get_default_rangefinder()
reflectance = Reflectance.get_default_reflectance()
servo_one = Servo.get_default_servo(index=1)
servo_two = Servo.get_default_servo(index=2)
webserver = Webserver.get_default_webserver()
board = Board.get_default_board()
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
linearray = LineArray(i2c)
display = XrpDisplay()

drivetrain.set_zero_effort_behavior(True) # set motors to brake when effort is zero, rather than coasting. 

if hasattr(Pin.board, "SERVO_3"):
    servo_three = Servo.get_default_servo(index=3)
if hasattr(Pin.board, "SERVO_4"):
    servo_four = Servo.get_default_servo(index=4)