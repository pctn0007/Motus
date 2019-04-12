# MOTUS "The Portable Security System"
# LOGIC FILE / SENSOR PERFORMANCE

# MOTION SENSOR - Will be active under GPIO 4
# LED - Will be active under GPIO 17
# ACCELEROMETER - Will be active under I2C 0x53
# FIREBASE - Will be active under database: ExampleProg

# MOTUSLOGIC.py Program by Dariusz Kulpinski
# Database Functions and Comms. by Anthony Pacitto
# Shell file to run camera function: CAMERA.sh
# Shell file to run image handling: IMAGE.sh

# UPDATED: 2019-04-11

# DECLARATIONS AND INITIALIZATION ------------------------------------------

import smbus
import time
import os
import datetime
import signal
import sys
import random
import json
import RPi.GPIO as GPIO
from google.cloud import storage
from firebase import firebase
from time import gmtime, strftime

# MACROS -------------------------------------------------------------------

sensitivity = 10 # The Accelerometers Sensetivity for Detection
                 # 0 = MAX Sensitivity | Any positive value = less sensitive

refreshrate = 1.0 # TIME BETWEEN CHECKS FOR SECURITY BREACHES

sleeptime = 10.0 # Suspend Time after Security Trigger
                 # SECONDS.MILLISECONDS

dcheck = 0       #Prevention of Double Movement Detection 
				 
boxid = '1'      # unique Box ID
				
pic = '/home/pi/SECURITYIMAGE.jpg' # snapshot file name
			# TO BE UPLOADED TO DATABASE
							
imagetosend = 'null' # initial image name
	             # RANDOMLY GENERATED THROUGH CODE
			
# Motion types (i.e. case motion vs. stimuli motion).
MOTION_TYPE_I2C = '0' #case
MOTION_TYPE_GPIO = '1' #stimuli

#INTERRUPT Catcher
def signal_handler(sig, frame):
    GPIO.output(17,GPIO.LOW)
    sys.exit(0);
signal.signal(signal.SIGINT, signal_handler)

# Get I2C bus
bus = smbus.SMBus(1)

# Get Firebase Connection
firebase = firebase.FirebaseApplication('https://exampleprog-69f69.firebaseio.com/', None)
credential_path = "/home/pi/Exampleprog.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
client = storage.Client()
bucket = client.get_bucket('exampleprog-69f69.appspot.com')

# Get GPIO devices
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT) # LED LIGHT ADDRESS
GPIO.setup(4,GPIO.IN)   # MOTION SENSOR ADDRESS
GPIO.output(17,GPIO.HIGH) #Default LED STATUS set to HI for power status

# PRIMARY LOGIC LOOP (NO MORE INITIALIZATION) ------------------------------------------

xAcclafter = 0   # Motion Defaults Set
yAcclafter = 0   # For X , Y, Z
zAcclafter = 0   # Axis'

print("MOTUS is ready to defend. Waiting for event...")
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
    if(dcheck is 0 and xAcclafter is not 0 and yAcclafter is not 0 and zAcclafter is not 0):
    
        xChange = xAcclbefore - xAcclafter
        yChange = yAcclbefore - yAcclafter
        zChange = zAcclbefore - zAcclafter
        
        if(xChange >= sensitivity or xChange <= -sensitivity or
           yChange >= sensitivity or yChange <= -sensitivity or
           zChange >= sensitivity or zChange <= -sensitivity):
            
            print("MOVEMENT DETECTED ON THE DEVICE")
            dtime = strftime("%d %b %Y %H:%M:%S", gmtime()) # detection timestamp
            imagetosend = (strftime("%d%b%Y_%H_%M_%S.jpg", gmtime()))
            GPIO.output(17,GPIO.LOW)
            time.sleep(0.4)
            GPIO.output(17,GPIO.HIGH)
            time.sleep(0.4)
            GPIO.output(17,GPIO.LOW)
				
            #CAMERA CALL
            os.system("./CAMERA.sh")
				
            #DATABASE INSERTION
            data = {'BoxID': boxid,'Picture': imagetosend,'Date': dtime,'SType': MOTION_TYPE_I2C}
            sent = json.dumps(data)
            result = firebase.post('/Detections/', data)
				
	    #IMAGE INSERTION
            zebraBlob = bucket.blob("Detections/" + imagetosend)
            zebraBlob.upload_from_filename(filename=pic)
            
            print("Data Uploaded Succesfully. Alert sent to database.")
                
            # COOLDOWN / IMAGE HANDLING
            os.system("./IMAGE.sh")
            time.sleep(sleeptime) #Trigger Cooldown
            print("COOLDOWN EXPIRE - %d SECONDS" %sleeptime)
            dcheck = 1 # PREVENTION OF REPEAT
    else:
        dcheck = 0 # PREVENTION OF REPEAT
                
    # End Movement Check
                
    # Assign Values for Next Movement Check
    xAcclafter = xAcclbefore
    yAcclafter = yAcclbefore
    zAcclafter = zAcclbefore
    
    # MOTION SENSOR DETECTION ------------------------------------------------------
    
    motion = GPIO.input(4) # HI | LO assignment to motion
        
    if motion is 1: # if motion is HI
            
        print("MOTION DETECTED TOWARDS THE DEVICE")
        dtime = strftime("%d %b %Y %H:%M:%S", gmtime()) # detection timestamp
        imagetosend = (strftime("%d%b%Y_%H_%M_%S.jpg", gmtime()))
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
		
        #CAMERA CALL / IMAGE SETUP
        os.system("./CAMERA.sh")
        #DATABASE INSERTION
        data = {'BoxID': boxid,'Picture': imagetosend,'Date': dtime,'SType': MOTION_TYPE_GPIO}
						
        sent = json.dumps(data)
        result = firebase.post('/Detections/', data)
	
	#IMAGE INSERTION
        zebraBlob = bucket.blob("Detections/" + imagetosend)
        zebraBlob.upload_from_filename(filename=pic)
				
        print("Data Uploaded Succesfully. Alert sent to database.")
        
        # COOLDOWN / IMAGE HANDLING
        os.system("./IMAGE.sh")
        time.sleep(sleeptime)
        print("COOLDOWN EXPIRE - %d SECONDS" %sleeptime)
        
    # End Motion Check

    time.sleep(refreshrate) # REFRESH RATE OF CHECKS
    GPIO.output(17,GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(17,GPIO.HIGH)
       
# END PROGRAM ==================================================================
