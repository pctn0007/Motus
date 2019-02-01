import random
from firebase import firebase

firebase = firebase.FirebaseApplication('https://motus-e3989.firebaseio.com/random', None)

result = firebase.post('/coupons',{'ID':random.randrange(100000, 999999, 6)})

print(result)
