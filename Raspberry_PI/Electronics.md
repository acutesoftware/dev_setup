## Electronic Circuits for Raspberry PI Zero
Examples of home built add-ons for the Raspberry PI Zero W

See - https://learn.adafruit.com/playing-sounds-and-using-buttons-with-raspberry-pi?view=all

### Attach a LED

connect a LED via resistor to pin 17


### Attach a switch as Input

3.3v --> 10k Pull-up Resistor --> GPIO --> Button --> GND



### Simple Photocell Reading on Digital Input

This allows you to get a very rough indication of light / dark / dim lights - enough for 
a home automation monitor at least, and it doesnt need an ADC

See https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi?view=all#

3.3v --> Photocell --> GPIO --> (+) 1uF Capacitor (-) --> GND

Use the sample code below to continuously poll the photocell for a very rough reading-on-raspberry-pi


~~~

import RPi.GPIO as GPIO, time, os      
GPIO.setmode(GPIO.BCM)
 
def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.1)
 
        GPIO.setup(RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading
 
while True:                                     
        print RCtime(18)     # Read RC timing using pin #18
        
~~~



