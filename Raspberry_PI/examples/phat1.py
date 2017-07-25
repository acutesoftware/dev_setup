#!/usr/bin/python3
# -*- coding: utf-8 -*-
# phat1.py 

import colorsys
import time
import subprocess
import phatbeat


@phatbeat.on(phatbeat.BTN_REWIND)
def button_RW(pin):
    play_sound('ouch')

@phatbeat.on(phatbeat.BTN_FASTFWD)
def button_FF(pin):
    play_sound('hello')

@phatbeat.on(phatbeat.BTN_PLAYPAUSE)
def button_play(pin):
    rainbow()

def main():

    print('ACTIVATED')
    try:
        while True:
            time.sleep(1)
            phatbeat.set_all(0,0,0)

    except KeyboardInterrupt:
        pass



def play_sound(wav_name):
    player = subprocess.Popen(["aplay", wav_name + ".wav"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def rainbow():
    SPEED = 300
    BRIGHTNESS = 64
    SPREAD = 20

    #while True:
    for cycles in range(1, 200):
        for x in range(phatbeat.CHANNEL_PIXELS):
            h = (time.time() * SPEED + (x * SPREAD)) % 360 / 360.0
            r, g, b = [int(c*BRIGHTNESS) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
            phatbeat.set_pixel(x, r, g, b, channel=0)
            phatbeat.set_pixel(x, r, g, b, channel=1)

        phatbeat.show()
        time.sleep(0.001)
    time.sleep(0.1)
    phatbeat.set_all(0,0,0)


        
if __name__ == "__main__":
    main()    