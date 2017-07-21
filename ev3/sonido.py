#!/usr/bin/env python3

from time import sleep
from ev3dev.ev3 import *

m = input("Que dira?: ")

Sound.speak(m).wait()

