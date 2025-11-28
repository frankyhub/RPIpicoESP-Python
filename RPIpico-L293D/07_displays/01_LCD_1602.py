## --------  LED (Digital Output)  ------- ##
#      tested with tinkertanks frisbee      #

# easy use with I2C Backback HW-61

import board, busio
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

i2c = busio.I2C(board.GP13, board.GP12)
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

lcd.clear()
lcd.set_cursor_pos(0, 1)
lcd.print("LOADING...")

# other commands:
lcd.shift_display(0)
lcd.set_backlight(1)
while True:
    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print("LEDS ON")
    lcd.set_cursor_pos(1,0)
    blink.animate()
    time.sleep(0.05)
    blink.animate()
    time.sleep(0.5)
    blink.animate()
    time.sleep(0.05)
    motor1.throttle = 0.125
    


