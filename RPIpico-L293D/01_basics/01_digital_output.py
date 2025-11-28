## --------  LED (Digital Output)  ------- ##
#      tested with tinkertanks frisbee      #

import time, board, digitalio

pin = digitalio.DigitalInOut(board.LED)    	# LED an Pin 12
pin.direction = digitalio.Direction.OUTPUT 		# Pin auf Output setzen

while True:
    pin.value = True
    time.sleep(1)
    print("on")
    
    pin.value = False
    time.sleep(1)
    print("off")