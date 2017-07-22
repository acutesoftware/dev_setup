## Utils - Windows
Processes and misc. techniques for the Raspberry PI Zero W using Windows

Based on https://www.raspberrypi.org/magpi/back-up-raspberry-pi/


### Backing up the PI with Windows

Once you've setup the PI so that it is working well, you can backup 
the entire OS and data using the following technique.

1. Shutdown the PI 
2. Remove the MicroSD card and plug into a card reader on your Windows PC
3. Download and install [Win32 Disk Imager](https://sourceforge.net/projects/win32diskimager/)
4. Run Win32DiskImager and enter "C:\rasp.img" into the Image File text box
5. Click Read and wait a few minutes for the image to be saved to your hard drive

### Restoring the PI with Windows

1. Insert a new blank MicroSD card into the Card reader on your PC
2. Run Win32DiskImager and click the folder icon to browse for your saved image "C:\rasp.img"
3. Click Write and wait a few minutes
4. Once done, safely eject the SD card and plug into your PI and power up


### Useful Scripts

Reboot

~~~
    sudo shutdown -r -t now
~~~

Find Available Wifi SSID's

~~~
    sudo iwlist wlan0 scan | grep ESSID
~~~

Find Network Neighbours

~~~
    ip -s n
~~~

Check CPU Info and Temperature

~~~
    cat /proc/cpuinfo
    vcgencmd measure_temp
~~~
   
 

