#!/usr/bin/env python3.6

import hashlib
import os
import time
from datetime import datetime, timedelta


yesterday = (datetime.now() - timedelta(days=1)).strftime("%m-%d-%Y")
today = time.strftime("%m-%d-%Y")

print('#########  Script started at: {}  ##########'.format(time.strftime("%d-%m-%Y %H:%M:%S")))

#Examples 

#SW check

path1 = '/path_to_backup/SW0/' + today
path2 = '/path_to_backup/SW0/' + yesterday


try:
    a = hashlib.md5(open(path1, 'rb').read()).hexdigest()
    b = hashlib.md5(open(path2, 'rb').read()).hexdigest()
except FileNotFoundError:
    print('####  File in SW0/* not found  #####')


try:
    if a != b:
        print("SW backup has Different files")
    else:
        print('Files in SW backup the same')
        os.remove(path1)
        print('{} removed'.format(path1))
except Exception :
    print('SW diff crashed')

print('*** diff in SW is ended ***')

#ASA check

path3 = '/path_to_backup/ASA/' + today
path4 = '/path_to_backup/ASA/' + yesterday


try:
    c = hashlib.md5(open(path3, 'rb').read()).hexdigest()
    d = hashlib.md5(open(path4, 'rb').read()).hexdigest()
except FileNotFoundError:
    print('####  File in ASA/* not found  #####')


try:
    if c != d:
        print("ASA backup has Different files")
    else:
        print('Files in ASA backup the same')
        os.remove(path3)
        print('{} removed'.format(path3))
except Exception :
    print('ASA diff crashed')

print('*** diff in ASA is ended ***')

# Extreme212

path13 = '/path_to_backup/Of-212/Extreme-210/' + today
path14 = '/path_to_backup/Of-212/Extreme-210/' + yesterday


try:
    a = hashlib.md5(open(path13, 'rb').read()).hexdigest()
    b = hashlib.md5(open(path14, 'rb').read()).hexdigest()
except FileNotFoundError:
    print('####  File in /Of-212/Extreme-210/* not found  #####')


try:
    if a != b:
        print("Extreme backup has Different files")
    else:
        print('Files of Extreme backup the same')
        os.remove(path13)
        print('{} removed'.format(path13))
except Exception :
    print('Extreme diff crashed')

print('*** diff in Extreme is ended ***')