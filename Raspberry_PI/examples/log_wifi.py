#!/usr/bin/python3
# -*- coding: utf-8 -*-

from wifi import Cell
from wifi import Scheme


def log_ssids():
    """
    scan for local Wifi points and log the SSID's to file
    """
    print('Scanning for wifi access points...')
    ssids = [cell.ssid for cell in Cell.all('wlan0')]
    with open('ssids.lis', 'w') as f:
        for s in ssids:
            f.write(s + '\n')

            
if __name__ == "__main__":
    log_ssids()