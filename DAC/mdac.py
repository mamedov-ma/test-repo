import RPi.GPIO as GPIO
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

    #time.sleep(0.1)

        

def repdac(repnumber):
    
    for j in range (0, repnumber):    
        for i in range (0,255):
            dnum2dac(i)
            #time.sleep(1)
            GPIO.output(D,0)


    
def sin(time_, samplingFrequence, frequence):   
    samplingFrequence = 1 / samplingFrequence
    for i in range(0, round(time_ / samplingFrequence)):
        x = round(abs(math.sin((i * frequence * 2 * math.pi) * samplingFrequence)) * 255)
        print(x)
        dnum2dac(x)
        time.sleep(samplingFrequence)
    
    Time = np.arange(0, time_, samplingFrequence)
    amplitude = np.sin(Time * 2 * math.pi * frequence)
    plt.plot(Time, amplitude)
    plt.title('sin')
    plt.xlabel('time')
    plt.ylabel('sin(time)')
    plt.minorticks_on()
    plt.show()
   
try:

    #sin(10, 100, 1)
    time_ = int(input())
    samplingfreq = int(input())
    sinfreq = int(input())
    sin(time_, samplingfreq, sinfreq)  
   
    
    
except ValueError:
    print('WTF???')

except Exception:
    print(' U OKAY?')


finally:
    GPIO.output(D,0)
    GPIO.cleanup()