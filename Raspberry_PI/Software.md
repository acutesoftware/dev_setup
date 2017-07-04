## Software for the Raspberry PI Zero
Examples of Python scripts for the Raspberry PI Zero W

### Setup environment for Python 3

~~~

sudo apt-get install python3-pip
sudo pip3 install wifi

~~~


### Test the wifi 

Quick script to scan for wifi access points

~~~

#!/usr/bin/python3
from wifi import Cell, Scheme
def main():
    print('Scanning for wifi access points...')
    ssids = [cell.ssid for cell in Cell.all('wlan0')]
    with open('ssids.lis', 'w') as f:
        for s in ssids:
            f.write(s + '\n')
main()

~~~


### Flash an LED

todo


## Setup Audio - USB Audio Adapter

todo 





## Setup Audio Input - via Adafruit I2S MEMS Microphone Breakout 

https://learn.adafruit.com/adafruit-i2s-mems-microphone-breakout/raspberry-pi-wiring-and-test

Allow I2S use

~~~
sudo nano /boot/config.txt
~~~

and Uncomment #dtparam=i2s=on


Make sure kernal allows sound 

~~~
sudo nano /etc/modules
~~~

and add the line snd-bcm2835


Compile the Kernal (can take an hour on the PI Zero)

~~~
sudo apt-get install rpi-update
sudo rpi-update

sudo apt-get install bc libncurses5-dev

sudo wget https://raw.githubusercontent.com/notro/rpi-source/master/rpi-source -O /usr/bin/rpi-source
sudo chmod +x /usr/bin/rpi-source
/usr/bin/rpi-source -q --tag-update
rpi-source

~~~



