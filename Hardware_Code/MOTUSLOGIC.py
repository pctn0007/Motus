# MOTUS "The Portable Security System"
# LOGIC FILE / SENSOR PERFORMANCE

# MOTION SENSOR - Will be active under GPIO 4
# LED - Will be active under GPIO 17
# ACCELEROMETER - Will be active under I2C 0x53

# MOTUSLOGIC.py Program by Dariusz Kulpinski
# Database Functions and Comms. by Anthony Pacitto
# Shell file to run camera function: MOTUSCAMERA.sh

# DECLARATIONS AND INITIALIZATION --------------------------------------

import smbus
import time
import os
import RPi.GPIO as GPIO
import time

# MACROS

sensitivity = 20 # The Accelerometers Sensetivity for Detection
                 # 0 = Most Sensitive | Any positive value = less sensitive

sleeptime = 3.0 # Suspend Time after Security Trigger
                 # SECONDS.MILLISECONDS

# Get I2C bus
bus = smbus.SMBus(1)

# Get GPIO devices
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT) # LED LIGHT ADDRESS
GPIO.setup(4,GPIO.IN)   # MOTION SENSOR ADDRESS
GPIO.output(17,GPIO.HIGH) #Default LED STATUS set to HI for power status

# PRIMARY LOGIC LOOP (NO MORE INITIALIZATION) ---------------------------

xAcclafter = 0   # Motion Defaults Set
yAcclafter = 0   # For X , Y, Z
zAcclafter = 0   # Axis'

while True:

# ADXL345 MOTION OBSERVATION LOGIC

    bus.write_byte_data(0x53, 0x2C, 0x0A)
    bus.write_byte_data(0x53, 0x2D, 0x08)
    bus.write_byte_data(0x53, 0x31, 0x08)

    time.sleep(0.5) #Refresh Rate

    data0 = bus.read_byte_data(0x53, 0x32)
    data1 = bus.read_byte_data(0x53, 0x33)

    xAcclbefore = ((data1 & 0x03) * 256) + data0
    if xAcclbefore > 511 :
            xAcclbefore -= 1024

    data0 = bus.read_byte_data(0x53, 0x34)
    data1 = bus.read_byte_data(0x53, 0x35)

    yAcclbefore = ((data1 & 0x03) * 256) + data0
    if yAcclbefore > 511 :
            yAcclbefore -= 1024

    data0 = bus.read_byte_data(0x53, 0x36)
    data1 = bus.read_byte_data(0x53, 0x37)

    zAcclbefore = ((data1 & 0x03) * 256) + data0
    if zAcclbefore > 511 :
            zAcclbefore -= 1024

# IF MOVEMENT HAS BEEN DETECTED ON THE DEVICE ----------------------------------
    
    # Skips the Initialization values on first loop
    if(xAcclafter is not 0 and yAcclafter is not 0 and zAcclafter is not 0):
    
        xChange = xAcclbefore - xAcclafter
        yChange = yAcclbefore - yAcclafter
        zChange = zAcclbefore - zAcclafter
        
        if(xChange >= sensitivity or xChange <= -sensitivity or
           yChange >= sensitivity or yChange <= -sensitivity or
           zChange >= sensitivity or zChange <= -sensitivity):
            
                print("MOVEMENT DETECTED ON THE DEVICE")
                GPIO.output(17,GPIO.LOW)
                time.sleep(0.4)
                GPIO.output(17,GPIO.HIGH)
                time.sleep(0.4)
                GPIO.output(17,GPIO.LOW)
                time.sleep(0.4)
                GPIO.output(17,GPIO.HIGH)
                #CAMERA CALL
                os.system("./MOTUSCAMERA.sh")
                #DATABASE INSERTION
                
                # COOLDOWN
                time.sleep(sleeptime) #Trigger Cooldown
                print("COOLDOWN EXPIRE - %d SECONDS" %sleeptime)
                
    # End Movement Check
                
# Assign Values for Next Movement Check

    xAcclafter = xAcclbefore
    yAcclafter = yAcclbefore
    zAcclafter = zAcclbefore
    
    # MOTION SENSOR DETECTION -------------------------------------------------
    
    motion = GPIO.input(4)
        
    if motion is 1:
            
        print("MOTION DETECTED TOWARDS THE DEVICE")
        GPIO.output(17,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(17,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(17,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(17,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(17,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(17,GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(17,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(17,GPIO.HIGH)
        #CAMERA CALL
        os.system("./MOTUSCAMERA.sh")      
        #DATABASE INSERTION
        
        # COOLDOWN
        time.sleep(sleeptime) #Trigger Cooldown
        print("COOLDOWN EXPIRE - %d SECONDS" %sleeptime)
        
    # End Motion Check

# END PROGRAM
                

