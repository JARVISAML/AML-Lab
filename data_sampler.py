import serial
import numpy as np
import pandas as pd
import time

class Sampler:
    def __init__(self, port='COM6', baud=115200):
        self.port = port
        self.baud = baud
        self.timeout = 5
        self.temp_set = 0
        self.count = 0
        self.ard = serial.Serial(self.port,self.baud,self.timeout)
        self.temperature_setter()
        self.remove_rand()

    def remove_rand(self):
        for i in range(8):
            info = self.ard.readline()
            elem=info.decode()
            #print(elem)

    def temperature_setter(self):
        while(self.temp_set<2): 
            time.sleep(2)
            self.ard.write(bytes('t\n', 'utf-8'))
            self.temp_set+=1

    def remove_newline(self, string):
        new_line='\r\n'
        if new_line in  string:
            new_str=string.replace(new_line,'')
            return new_str

    def collect(self): 
        itr = 3
        arr=[]     
        i= 0  
        calc = 0
        prev = 0
        info = self.ard.readline()
        if(itr < 5):
            itr +=1

        else:
            while(1):    
                elem=info.decode()
                if len(elem)!=0:
                    elem=elem.split(',')
                    last_elem=elem[len(elem)-1]
                    cleaned = self.remove_newline(last_elem)
                    elem[len(elem)-1]=cleaned
                    for i in range(len(elem)):
                        elem[i]=float(elem[i])
                    calc = sum(elem)
                    
                    if calc != prev:
                        arr.append(elem)
                        prev = calc
                        self.count +=1

                    if(self.count == 5):

                        final=np.zeros((17))
                        mat=np.asarray(arr)
                        rows=mat.shape[0]
                        columns=mat.shape[1]
                        for i in range(columns): 
                            sums=0
                            avg=0
                            col=mat[:,i]
                            for elem in col:
                                sums=sums+elem
                            avg=sums/len(col)
                            final[i]=avg
                        self.count = 0
                        return final