#Schaltuhr.py

from gpiozero import LED, TimeOfDay
from datetime import time
from signal import pause

led1 = LED(17)
led2 = LED(22)

tod1 = TimeOfDay(time(8,51), time(8,55), utc=False)
tod2 = TimeOfDay(time(8,53), time(8,59), utc=False)

tod1.when_activated = led1.on
tod1.when_deactivated = led1.off

tod2.when_activated = led2.on
tod2.when_deactivated = led2.off

pause()