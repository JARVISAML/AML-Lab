import keyboard
import serial
import numpy as np
import pandas as pd
import xlsxwriter


file='C:/Users/TarekLEGION/Desktop/trialw.xlsx'
workbook = xlsxwriter.Workbook(file)
worksheet = workbook.add_worksheet()



port = 'COM4'

# ard = serial.Serial(port,9600,timeout=5)


row=0
dummy=[i for i in range(16)]
arr=[]

while(1):
    
    
    
    
     
     print('s>>start colletion ')
     print('q>>stop--log to csv')
     print('r>>restart')
    
     key_pressed=keyboard.read_key()
     if key_pressed=='s':
         
         while(keyboard.read_key()=='s'):
             arr.append(dummy)
             print('arr')
             
             
             
             
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
         
         
             
              for column,element in enumerate(final): 
                  worksheet.write(row,column,element)
                  
                  
              print ('Logged Succesfuly')
             


           
         
        
     if(key_pressed=='r'):
         row+=1
         print('restarting')
         arr=[]
         
    
     if (key_pressed=='x'):
         
         print('<<Terminating>>')
         break
     
workbook.close()
         
         
         
         
            # if flag==1:     
     #     print('hello')
     #     # info = ard.readline()
     #     # elem=info.decode()
     #     # arr.append(elem)
        
         
    
        
             
            
             
             
         
         
  
    

                
                
                
       
        
         
            
            
            
            
            
        
       
       
       
  
       
       