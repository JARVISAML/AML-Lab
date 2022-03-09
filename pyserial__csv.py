import keyboard
import serial
import numpy as np
import pandas as pd
import csv


file='C:/Users/TarekLEGION/Desktop/trial.csv'
port = 'COM4'

# ard = serial.Serial(port,9600,timeout=5)
flag=0
ctr=1 
    
     #     # info = ard.readline()
     
     #     # elem=info.decode()
     # elem=elem.split(',')
    
 #### UNCOMMENT AND REPLACE WITH DUMMY AFTER CHECKING SERIAL INPUT
         
dummy=[i for i in range(16)]
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
        

while(1):
    
    ###Uncomment for arduino
        
    # info = ard.readline()
         
    # elem=info.decode()
    # elem=elem.split(',')
    
    # print('before',elem) 
    # last_elem=elem[len(elem)-1]
    # cleaned=remove_newline(last_elem)
    # print('cleaned',cleaned)
    # elem[len(elem)-1]=cleaned
    # for i in range(len(elem)):
    #     elem[i]=float(elem[i])
        
    # print('final',elem)
    
    
     key_pressed=keyboard.read_key()
     if key_pressed=='s':
         while(keyboard.read_key()=='s'):
             arr.append(dummy)
             print('collecting')
             
             
             
             
     if (key_pressed=='q'):
         
         
         final=np.zeros((16))
         
         
         
         print('enter label (int)')
         # label=input()

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
         
         if input()=='y':
             
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
    