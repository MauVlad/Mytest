#import ev3dev.ev3 as ev3


from ev3dev.ev3 import *
from time import sleep

Sound.beep()
sleep(4)

Soun.beep().wait()
sleep(4)

Sound.tone(1500,2000).wait()
sleep(4)

Sound.paly('sounds/cat_yowl.wav').wait()
Sound.beep()
sleep(4)

Sound.paly('sounds/cat_yowl.wav')
Sound.beep() 
