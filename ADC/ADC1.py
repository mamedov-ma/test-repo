#import RPi.GPIO as GPIO
import numpy as np
import matplotlib.pyplot as plt
import time
import math

GPIO.cleanup()
D = [10, 9, 11, 5, 6, 13, 19, 26] 
GPIO.setmode(GPIO.BCM)
GPIO.setup(D, GPIO.OUT)

GPIO.output(D,0)


def decToBinList(decNumber):
    b = 1
    a = [0,0,0,0,0,0,0,0]

    for i in range(0,8):
        if (b & (decNumber >> i) == 1):
            a[7 - i] = 1
      
    print (a)
    return a



def dnum2dac(number):
    
    GPIO.output(D,0)
    A = decToBinList(number)
    
    for i in range (0,8):
        if A[i] == 1:
            GPIO.output(D[7 - i],1)




def finder(number):
    a = 128
    b = 128
    while(1):
         
        dnum2dac(a)
        
        if():
            a  = a + a / 2
        else:
            a = a - a / 2
        if(b - a == 0):
            break
        

    
    printf(a + 1, "V")

