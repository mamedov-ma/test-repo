from os.path import dirname, join as pjoin
from scipy.io import wavfile
import scipy.io
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
      
    #print (a)
    return a



def dnum2dac(number):
    
    GPIO.output(D,0)
    A = decToBinList(number)
    
    for i in range (0,8):
        if A[i] == 1:
            GPIO.output(D[7 - i],1)

   

        


   
data_dir = pjoin('/home', 'gr004', 'Desktop')
wav_fname = pjoin(data_dir,'SOUND.WAV')
samplerate, data = wavfile.read(wav_fname)
#print(f"number of channels = {data.shape[1]}")
length = data.shape[0] / samplerate
#print(f"length = {length}s")
#print(data.shape[0])
#print(samplerate)


for i in range(0, data.shape[0]):
        x = (data[i, 0] + 2048) / 4096 * 255
        #print(x)
        dnum2dac(round(x))
        time.sleep(1 / samplerate)


time_ = np.linspace(0, length, data.shape[0])
plt.plot(time_, data[:, 0], label="Left channel")   
plt.plot(time_, data[:, 1], label="Right channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()