import keyboard
import serial
import numpy as np
import pandas as pd
import csv
import time


file='C:\\Users\\gassa\\Desktop\\data\\santos_java.csv'
port = 'COM6'

ard = serial.Serial(port,115200,timeout=5)
flag=1
ctr=1 
hala=0
itr = 3
label = "santos_java"
    
     #     # info = ard.readline()
     
     #     # elem=info.decode()
     # elem=elem.split(',')
    
 #### UNCOMMENT AND REPLACE WITH DUMMY AFTER CHECKING SERIAL INPUT
         
dummy=[i for i in range(17)]
arr=[]

     
def log_to_csv(array,operation):
    
   
    with open(file,operation,newline='') as f:
        writer=csv.writer(f)
        writer.writerow(array)
        
        

def print_menu():
 
    print('HOLD s listens for serial data>>start colletion ')
    print('press q>> average matrix andlog to csv')
    print('press r >> new sample')
    print('press x>> terminate')
    print('press h>> show menu again')
    
    
def remove_newline(string):
    
    new_line='\r\n'

    if new_line in  string:
        print('present')
     
        new_str=string.replace(new_line,'')
        return new_str
    
    else:
        print('clean')
        
i=0
    

print_menu()

while(hala<2): 
     time.sleep(2)
     ard.write(bytes('t\n', 'utf-8'))
     hala+=1

print('STARTING BITCHEzzzzzzzzzz')
time.sleep(15)     
for i in range(8):
    info = ard.readline()
    elem=info.decode()
    print(elem)



calc = 0
prev = 0
state = 0

while(1):
    
    ###Uncomment for arduino
    info = ard.readline()
    if(itr < 5):
        itr +=1

    else:    
        elem=info.decode()
        if len(elem)!=0:
            elem=elem.split(',')

        
            print('before',elem) 
            last_elem=elem[len(elem)-1]
            cleaned=remove_newline(last_elem)
            print('cleaned',cleaned)
            elem[len(elem)-1]=cleaned
            for i in range(len(elem)):
                elem[i]=float(elem[i])
            
            print('element appended',elem)

            calc = sum(elem)

        
            key_pressed=keyboard.read_key()
            
            if calc != prev and state == 0:
                arr.append(elem)
                print('collecting')
                prev = calc
                    
                
                
                
                
            if(key_pressed=='q'):
                save_it = 0
                while(save_it != 1):
                
                    state = 1



                    
                    
                    final=np.zeros((17))
                    
                    
                    
                    print('enter label (int)')
                    #label=label

                    mat=np.asarray(arr)
                    rows=mat.shape[0]
                    columns=mat.shape[1]
                    
                    print('matrix',mat)
                    print('averaging')
                    
                    for i in range(columns): 
                        sums=0
                        avg=0
                        
                        col=mat[:,i]
                        
                        for elem in col:
                            sums=sums+elem
                            
                        avg=sums/len(col)
                        
                        final[i]=avg
                        
                    print('final_matrix',final)
                    
                    
                    print('Log to csv? [y/n]')

                    if input()=='n':
                        print(final)
                        save_it = 1
                    
                    elif input()=='y':
                        save_it = 1
                        final[16] = float(1.0)
                        print("measurements: ", rows)
                        
                        print('logging to csv')
                        
                        if(flag==0):
                            
                            ####Write in first acess to file####
                            
                            log_to_csv(final,'w')
                            flag=1
                            
                            
                        elif flag==1:
                            ####Append to file after
                            log_to_csv(final,'a')
                            
                        print('Logged succesfully')
                    
            
                        
                
                
            if(key_pressed=='r'):
                print(f'sample {ctr} done')
                ctr+=1
                print_menu()
                arr=[]
                
            if (key_pressed=='h'):
                print_menu()
                
            
            if (key_pressed=='x'):
                
                print('<<Terminating>>')
                break
        