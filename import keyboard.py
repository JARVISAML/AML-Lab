import keyboard
import serial
import numpy as np
import pandas as pd
import csv


file='C:\\Users\\gassa\\Desktop\\data\\trial.csv'
port = 'COM6'
ard = serial.Serial(port,115200,timeout=5)
flag=0
ctr=1 
    
info = ard.readline()
     
elem=info.decode()
elem=elem.split(',')

print(elem)