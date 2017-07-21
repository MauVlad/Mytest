""" Sound capabilities demonstration.
"""

from textwrap import dedent
import os

##import ev3dev.ev3 as ev3
from ev3dev.ev3 import Sound

_HERE = os.path.dirname(__file__)

print(dedent("""
    A long time ago
    in a galaxy far,
    far away...
	"""))

Sound.play_song((
    ('D4', 'e3'),
    ('D4', 'e3'),
    ('D4', 'e3'),
    ('G4', 'h'),
    ('D5', 'h'),
    ('C5', 'e3'),
    ('B4', 'e3'),
    ('A4', 'e3'),
    ('G5', 'h'),
    ('D5', 'q'),
    ('C5', 'e3'),
    ('B4', 'e3'),
    ('A4', 'e3'),
    ('G5', 'h'),
    ('D5', 'q'),
    ('C5', 'e3'),
    ('B4', 'e3'),
    ('C5', 'e3'),
    ('A4', 'h.'),
)).wait()


Sound.play(os.path.join(_HERE, 'snd/r2d2.wav')).wait()


Sound.speak("Luke, I am your father").wait()
