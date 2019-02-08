import random
import json
import time

from firebase import firebase
from time import gmtime, strftime

#GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(4,GPIO.IN)
GPIO.output(17,GPIO.LOW)

# Database root
firebase = firebase.FirebaseApplication('https://motus-e3989.firebaseio.com/', None)

# Database Detection data
boxid = 'm1'
udid =  random.randrange(100000, 999999, 6)
pic = 'test.jpg'
dtime = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())


# MotionSensor detection


# JSON object to INSERT
data = {'Uid': uid,
        'Picture': pic,
        'Date': dtime}
sent = json.dumps(data)

# Database path to INSERT data
result = firebase.post('/Detections/' + boxid, data)

print(result)
