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

G = [24,25,8,7,12,16,20,21] 
GPIO.setmode(GPIO.BCM)
GPIO.setup(G, GPIO.OUT) 
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

def dnum1dac(number):
    
    GPIO.output(D,0)
    A = decToBinList(number)
    
    for i in range (0,8):
        if A[i] == 1:
            GPIO.output(G[7 - i],1)



def finder():
    a = 128
    for i in range (0,7):
        #a = round(a)
        dnum2dac(a)
        time.sleep(0.001)
        if(GPIO.input(4) == 1):
            a = a + 2 ** (6 - i)
        else:
            a = a - 2 ** (6 - i)
        #print(a)
    if(a == 1):
        a = a - 1
    if (a < 32):
        dnum1dac(1)
        return
    if (a > 32 and a < 64):
        dnum1dac(3)
        return
    if (a > 64 and a < 96):
        dnum1dac(7)
        return
    if (a > 96 and a < 128):
        dnum1dac(15)
        return
    if (a > 128 and a < 160):
        dnum1dac(31)
        return
    if (a > 160 and a < 192):
        dnum1dac(63)
        return
    if (a > 192 and a < 224):
        dnum1dac(127)
        return
    if (a > 224 and a < 256):
        dnum1dac(255)
        return

        
while True:
    finder() 
    time.sleep(0.1)
    
    GPIO.output(G,0)
    

