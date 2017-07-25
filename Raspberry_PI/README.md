## Dev_setup - Raspberry PI Testing
Scripts to test the Raspberry PI Zero W

See also 
[Hardware](https://github.com/acutesoftware/dev_setup/blob/master/Raspberry_PI/Hardware.md)<br />

https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md

https://www.piborg.org/blog/pi-zero-wifi-bluetooth

http://tutorial.cytron.com.my/2017/05/02/getting-started-raspberry-pi-zero-w/



### Hardware unpacking and connections

- connect HDMI adapter to mini hdmi output, then attach screen to that

- connect OGT cable to mini usb port

- connect keyboard to usb OGT cable

- connect power cable (USB to mini) to raspberrypi

- connect a phone charging battery pack and turn on


You should see the raspberry PI linux boot sequence and will be presented with a logon screen

~~~

    login
        user: pi
        password: raspberry
    
~~~    

### Connecting to wifi via command line


Open the wpa-supplicant configuration file in nano:

~~~
    sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
~~~

Go to the bottom of the file and add the following:

~~~
    network={
        ssid="[your_wifi_name]"
        psk="[your_wifi_password]"
        key_mgmt=WPA-PSK
    }
~~~

Then reboot using the command

~~~
    sudo shutdown -r -t now
~~~

When it reboots it should pick up an ip address and have internet connectivety.

Write down the ip address ( in this case it was 192.168.1.7 )

To check this ping google via 

~~~
    ping www.google.com
~~~

### Optional - use the raspi-config tool to set locale

Note the kit I got was set to UK, so if in Australia set your country using 

~~~    
    sudo raspi-config
~~~

Follow the menu prompts to change the country and change your password here



### Go to headless mode and connect remotely

Once everything is working, you can disconnect the monitor and keyboard and connect from your desktop

Go to your desktop and in a command prompt, confirm you can connect to the pi

~~~
    ping 192.168.1.7    
~~~

If using Windows, install PuTTY and connect using SSH port 22 to the device



### Initial Software Setup

You now have a remote SSH connection to the Raspberry PI which is basically a Linux box, so install software as needed.

~~~~

    sudo apt-get update

    sudo apt-get install python3

    sudo apt-get install python3-gpiozero python-gpiozero

    sudo apt-get install --reinstall python-pkg-resources

    sudo apt-get install --reinstall python3-pkg-resources
    
~~~~


### Testing Python with the libraries

To make sure everything is good to go, create a python program as follows

~~~
nano test.py
~~~

and paste in the code below

~~~

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# test.py

from gpiozero import LED
from time import sleep

led = LED(17)
led.on()

~~~

change the permissions to allow it to be executed

~~~
chmod +x test.py

./test.py

~~~


The program will run and return nothing. Ensure it doesnt have errors (it wont actually turn 
on the LED as we havent connected one yet) but this makes sure the 
libraries are all ready to go)


### Developing Python programmings locally
May be easier to write the programs on your desktop with your preferred IDE then transfer them to the PI


To do this:

1. Write your program on your desktop
2. Use Filezilla or another ftp program to transfer the program to the PI
3. Use PuTTY to run the program on the PI once transferred
 


### Next Steps
[Electronics](Electronics.md) - Ideas for circuits to attach via the GPIO<BR>
[Software](Software.md) - sample scripts to use on the PI Zero W<BR>

