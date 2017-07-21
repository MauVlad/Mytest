#!/usr/bin/env python3

import ev3dev.ev3 as ev3

m1 = ev3.MediumMotor('outA')
m2 = ev3.LargeMotor('outB')
m3 = ev3.LargeMotor('outC')

m1.stop(stop_action="hold")
m2.stop(stop_action="hold")
m3.stop(stop_action="hold")

m1.stop(stop_action="brake")
m2.stop(stop_action="brake")
m3.stop(stop_action="brake")

m1.stop(stop_action="coast")
m2.stop(stop_action="coast")
m3.stop(stop_action="coast")

m1.stop()
m2.stop()
m3.stop()
