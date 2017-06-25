#!/usr/bin/python3
# -*- coding: utf-8 -*-
# blink.py
# see https://www.raspberrypi.org/blog/gpio-zero-a-friendly-python-api-for-physical-computing/

from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
