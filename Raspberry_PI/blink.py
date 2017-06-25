#!/usr/bin/python3
# -*- coding: utf-8 -*-
# blink.py
# see https://www.raspberrypi.org/blog/gpio-zero-a-friendly-python-api-for-physical-computing/


def main():
    blink1()
    blink2()
    

def blink1():
    from gpiozero import LED
    from time import sleep

    led = LED(17)

    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)
    
 
def blink2():
    from gpiozero import LED, Button
    from signal import pause

    led = LED(17)
    button = Button(2)

    button.when_pressed = led.on
    button.when_released = led.off

    pause()
 
main()
    
