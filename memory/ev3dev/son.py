#import ev3dev.ev3 as ev3


from ev3dev.ev3 import *
from time import sleep

#Sound.beep()
#sleep(4)

#Sound.beep().wait()
#sleep(4)

#Sound.tone(1500,2000).wait()
#sleep(4)

Sound.play('chewy.wav').wait()
#Sound.beep()
sleep(4)

Sound.play('p/demo/misc/snd/r2d2.wav')
Sound.beep() 
