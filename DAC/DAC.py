import RPi.GPIO as GPIO
import numpy as np
#import matplotlib.pyplot as plt
import time

GPIO.cleanup()
D = [10, 9, 11, 5, 6, 13, 19, 26] 
GPIO.setmode(GPIO.BCM)
GPIO.setup(D, GPIO.OUT)



#time = np.arange(0, 50, 0.05)
#amplitude = np.sin(time)
#plt.plot(time, amplitude)
#plt.title('')
#plt.xlabel('')
#plt.ylabel(' sin(time)')
#plt.show()


def decToBinList(decNumber):
    b = 1
    a = [0,0,0,0,0,0,0,0]

    for i in range(0,8):
        if (b & (decNumber >> i) == 1):
            a[7 - i] = 1
      
    print (a)
    return a



def dnum2dac(number):
    A = decToBinList(number)
    
    for i in range (0,8):
        if A[i] == 1:
            GPIO.output(D[7 - i],1)
    
    #GPIO.output(D,0)


def repdac(repetitionnumber):
    
    for j in range (0, repetitionnumber):    
        repetitionnumber = repetitionnumber + 1
        for i in range (0,255):
            dnum2dac(i)
            time.sleep(0.2)
            GPIO.output(D,0)


#dnum2dac(255)
repdac(1)



