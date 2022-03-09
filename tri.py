import keyboard
import serial
import numpy as np
import pandas as pd
import csv
import time


file='C:\\Users\\gassa\\Desktop\\data\\trial.csv'
port = 'COM6'
ard = serial.Serial(port,115200,timeout=5)
flag=0
ctr=1
hala = 0


key_pressed = 0

while(hala<2): 
     info = ard.readline()
     elem=info.decode()

     elem=elem.split(',')
     key_pressed=keyboard.read_key()

     print(elem)
     time.sleep(2)
     ard.write(bytes('t\n', 'utf-8'))
     hala+=1

while(key_pressed!= 'q'):
    info = ard.readline()
    elem=info.decode()
    elem=elem.split(',')
    new = keyboard.read_key()
    key_pressed=keyboard.read_key()

    print(elem)