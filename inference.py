import serial
from joblib import dump, load
import time

port = 'COM6'
#ard = serial.Serial(port,115200,timeout=5)

clf = load('lgbm.joblib')

labels = {0:"water", 
 1:"santos_java",
 2:"guatemala_elephant",
 3:"san_agustin_colombia",
 4:"monsoon_malabar",
 5:"sumatra",
 6:"mocha_djimmah",
 7:"dominican_republic",
 8:"ethiopia_yirgacheffe",
 9:"kenya_peaberry",
 10:"coke",
 11:"lipton",
 12:"lucazade"}

while(True):
    prediction = clf.predict(X)
    print(labels[prediction])
    time.sleep(1)
