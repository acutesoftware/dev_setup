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

https://core-electronics.com.au/usb-audio-adapter-works-with-raspberry-pi.html

With the PI Zero turned off, plug in the Audio UBS adapter to the micro slot and plug in headphones

Power up the PI and logged in remotely


#### List of useful commands

List the available audio devices 

aplay -l 

~~~
pi@raspberrypi:~ $ aplay -l
**** List of PLAYBACK Hardware Devices ****
card 0: ALSA [bcm2835 ALSA], device 0: bcm2835 ALSA [bcm2835 ALSA]
  Subdevices: 8/8
  Subdevice #0: subdevice #0
  Subdevice #1: subdevice #1
  Subdevice #2: subdevice #2
  Subdevice #3: subdevice #3
  Subdevice #4: subdevice #4
  Subdevice #5: subdevice #5
  Subdevice #6: subdevice #6
  Subdevice #7: subdevice #7
card 0: ALSA [bcm2835 ALSA], device 1: bcm2835 ALSA [bcm2835 IEC958/HDMI]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
card 1: Device [USB Audio Device], device 0: USB Audio [USB Audio]
  Subdevices: 1/1
  Subdevice #0: subdevice #0

~~~


Check the audio modules

~~~
cat /proc/asound/modules

 0 snd_bcm2835
 1 snd_usb_audio

~~~


speaker-test

~~~

Playback device is default
Stream parameters are 48000Hz, S16_LE, 1 channels
Using 16 octaves of pink noise
Channels count (1) not available for playbacks: Invalid argument
Setting of hwparams failed: Invalid argument

~~~


#### Setup the Audio 

Following https://learn.adafruit.com/usb-audio-cards-with-a-raspberry-pi?view=all

~~~

sudo apt-get update
sudo apt-get upgrade
sudo reboot

~~~

Problem, is that the first step, I dont see the CM audio device so not sure if it will works-with-raspberry-pi
so ignored this step # sudo wget http://https://raw.github.com/Hexxeh/rpi-update/master/rpi-update -O /user/bin/rpi-update





~~~
sudo nano /etc/asound.conf
~~~

and add the following text

~~~
pcm.!default  {
 type hw card 1
}
ctl.!default {
 type hw card 1
}
~~~


trying speaker-test

~~~

Playback device is default
Stream parameters are 48000Hz, S16_LE, 1 channels
Using 16 octaves of pink noise
Channels count (1) not available for playbacks: Invalid argument
Setting of hwparams failed: Invalid argument


~~~



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



## Setup Pirate Radio

https://learn.pimoroni.com/tutorial/sandyj/internet-radio-on-your-pirate-radio

This works but if installing headless, you need to 
1. remove the HAT
2. Boot the PI
3. Login via SSH and run 

~~~
curl https://get.pimoroni.com/vlcradio | bash
~~~

Then shutdown, and plug in the HAT, then power up 

The radio will start automatically, use the pushbuttons to tune and control volume etc. 

Edit radio stations via 
 
 ~~~
 sudo nano /home/pi/.config/vlc/playlist.m3u
 ~~~
 
