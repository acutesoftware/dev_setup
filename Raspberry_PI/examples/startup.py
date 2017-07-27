#!/usr/bin/python3
# -*- coding: utf-8 -*-
# hat_startup.py 

import subprocess
import time


def startup_main():
    log_entry('startup_main called')
    time.sleep(5)
    play_sound('hello')

    
    log_entry('startup_main finished')
    

    
def log_entry(txt):
    with open('rasp.log', 'a') as f:
        f.write(txt + '\n')
    
def play_sound(wav_name):
    player = subprocess.Popen(["aplay", wav_name + ".wav"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    
    
startup_main()    