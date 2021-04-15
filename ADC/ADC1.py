import RPi.GPIO as GPIO
import numpy as np
import matplotlib.pyplot as plt
import time
import math

#GPIO.cleanup()
D = [10, 9, 11, 5, 6, 13, 19, 26] 
GPIO.setmode(GPIO.BCM)
GPIO.setup(D, GPIO.OUT)
GPIO.setup(4, GPIO.IN )
GPIO.setup(17, GPIO.OUT)
GPIO.output(17,1)
GPIO.output(D,0)


def decToBinList(decNumber):
    b = 1
    a = [0,0,0,0,0,0,0,0]

    for i in range(0,8):
        if (b & (decNumber >> i) == 1):
            a[7 - i] = 1
      
    #print (a)
    return a



def dnum2dac(number):
    
    GPIO.output(D,0)
    A = decToBinList(number)
    
    for i in range (0,8):
        if A[i] == 1:
            GPIO.output(D[7 - i],1)




def finder():
    
    for i in range(0,256):
         
        dnum2dac(i)
        time.sleep(0.00001)
        if(GPIO.input(4) == 0):
            #print(i / 256 * 3.3, "V")
            break
    print("Digital value:", i, ", Analog value:", i / 256 * 3.3, "V")
           
        
while True:
    finder() 
    


