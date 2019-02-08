import random
import json
import time

from firebase import firebase
from time import gmtime, strftime

# Database root
firebase = firebase.FirebaseApplication('https://motus-e3989.firebaseio.com/', None)

# Database Detection data
boxid = 'm1'   # unique motus bo id
uid =  'u1234' # unique user id via users table
pic = 'test-snapsot.jpg' # snapshot file name
dtime = strftime("%d %b %Y %H:%M:%S +0000", gmtime()) # detection timestamp (formatted)

# JSON object to INSERT
data = {'Uid': uid,
        'Picture': pic,
        'Date': dtime}
sent = json.dumps(data)

# Database path to INSERT data
result = firebase.post('/Detections/' + boxid, data)

print(result)
