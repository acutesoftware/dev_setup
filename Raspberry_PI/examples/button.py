#!/usr/bin/python3
# -*- coding: utf-8 -*-
# button.py
# see https://www.raspberrypi.org/blog/gpio-zero-a-friendly-python-api-for-physical-computing/


from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)

button.when_pressed = led.on
button.when_released = led.off

pause()
 