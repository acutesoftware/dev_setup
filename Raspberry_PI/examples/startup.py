#!/usr/bin/python3
# -*- coding: utf-8 -*-
# hat_startup.py 

import subprocess



def startup_main():
    play_sound('hello')


def play_sound(wav_name):
    player = subprocess.Popen(["aplay", wav_name + ".wav"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    
    
startup_main()    