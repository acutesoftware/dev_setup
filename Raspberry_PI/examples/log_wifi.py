#!/usr/bin/python3

from wifi import Cell, Scheme


def main():
    print('Scanning for wifi access points...')
    ssids = [cell.ssid for cell in Cell.all('wlan0')]
    with open('ssids.lis', 'w') as f:
        for s in ssids:
            f.write(s + '\n')

main()