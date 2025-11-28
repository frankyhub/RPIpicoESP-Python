## ------- NEOPIXEL BLINK ------- ##
#   tested with tinkertanks moon   #

import board, time, neopixel
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.chase import Chase


TEAL = (255,255,75)
RED = (255,0,0)

pixels1 = neopixel.NeoPixel(board.GP0, 64, brightness=0.5, auto_write=False)
pixels2 = neopixel.NeoPixel(board.GP27, 15, brightness=0.5, auto_write=False)
pixels3 = neopixel.NeoPixel(board.GP8, 100, brightness=0.5, auto_write=False)

blink1 = Blink(pixels1, speed=0.4, color=TEAL)
blink2 = Blink(pixels2, speed=0.5, color=RED)
chase = Chase(pixels3, speed=0.05, size=8, spacing=5, color=(125,125,255) )

while True:
    blink1.animate()
    blink2.animate()
    chase.animate()

