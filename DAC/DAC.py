import RPi.GPIO as GPIO
import numpy as np
import matplotlib.pyplot as plt
from time import sleep


D = [24,25,8,7,12,16,20,21] 
GPIO.setmode(GPIO.BCM)
GPIO.setup(D, GPIO.OUT)


time = np.arange(0, 50, 0.05)
amplitude = np.sin(time)
plt.plot(time, amplitude)
plt.title('Синус')
plt.xlabel('Время')
plt.ylabel('Амплитуда sin(time)')
plt.show()


def decToBinList(decNumber):
    b = 1
    a = [0,0,0,0,0,0,0,0]

    for i in range(0,8):
        if (b & (decNumber >> i) == 1):
            a[7 - i] = 1
      
    print (a)
    return a

 def dnum2dac(value):
     A = decToBinList(number)
    
    for i in range (0,8):
        if A[i] == 1:
        GPIO.output(D[7 - i],1)
    
    #GPIO.output(D,0)


def repdac(repetitionnumber):
    for i in range (0,255)
        dnum2dac(i)