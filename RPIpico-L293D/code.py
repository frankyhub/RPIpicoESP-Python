import board, time, neopixel
from adafruit_led_animation.animation.blink import Blink
import time, board, pwmio, digitalio
from adafruit_motor import motor
import board, busio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from adafruit_led_animation.animation.chase import Chase


TEAL = (255,255,75)

pixels = neopixel.NeoPixel(board.GP26, 48, brightness=0.5, auto_write=False)

blink = Blink(pixels, speed=0.01, color=TEAL)
pin = digitalio.DigitalInOut(board.GP2)    	# GP0 instead of LED for Pin D0
pin.direction = digitalio.Direction.OUTPUT 	# set gpio pin to 'output's
pin.value = 1

# OUTPUT 1
M1_A = board.GP3
M1_B = board.GP4
motor1 = motor.DCMotor(pwmio.PWMOut(M1_A, frequency=50), pwmio.PWMOut(M1_B, frequency=50))

i2c = busio.I2C(board.GP13, board.GP12)
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

pixels = neopixel.NeoPixel(board.GP8, 255, brightness=0.5, auto_write=False)

chase = Chase(pixels, speed=0.01, size=8, spacing=5, color=(125,125,255) )

lcd.clear()
lcd.set_cursor_pos(0, 1)
lcd.print("LOADING...")
lcd.shift_display(0)
lcd.set_backlight(1)
lcd.clear()
lcd.set_cursor_pos(0,0)
lcd.print("Motor ON")
lcd.set_cursor_pos(1,0)
lcd.print("LED ON")