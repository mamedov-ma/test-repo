import RPi.GPIO as GPIO
import time

D = [24,25,8,7,12,16,20,21] 
GPIO.setmode(GPIO.BCM)
GPIO.setup(D, GPIO.OUT)

#GPIO.output(D,1)
#time.sleep(3)
#GPIO.output(D,0)
#GPIO.cleanup(D)


def lightUp(ledNumber, period):
    
    GPIO.output(D[ledNumber],1)
    time.sleep(period)
    GPIO.output(D[ledNumber],0)
    GPIO.cleanup(D[ledNumber])

def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range (0, blinkCount):
        GPIO.output(D[ledNumber],1)
        time.sleep(blinkPeriod)
        GPIO.output(D[ledNumber],0)
        time.sleep(blinkPeriod)

def runningLight(count,period):
    for i in range (0, count):
        for j in range(0, 8):
            GPIO.output(D[j],1)
            time.sleep(period)
            GPIO.output(D[j],0)

def runningDark(count, period):
     GPIO.output(D,1)
     
     for i in range (0, count):
        for j in range(0, 8):
            GPIO.output(D[j],0)
            time.sleep(period)
            GPIO.output(D[j],1)
     GPIO.output(D,0)
    
            
def decToBinList(decNumber):
    b = 1
    a = [0,0,0,0,0,0,0,0]

    for i in range(0,8):
        if (b & (decNumber >> i) == 1):
            a[7 - i] = 1
      
    print (a)
    return a


def lightNumber(number):
    A = decToBinList(number)
        
    for i in range (0,8):
        if A[i] == 1:
            GPIO.output(D[7 - i],1)
            
    time.sleep(5)
    GPIO.output(D,0)
    
def runningPattern(pattern, direction):
    A = decToBinList(pattern)
    j = 0
    GPIO.output(D,0)
    while True:   

        for i in range (0,8):
            if A[i] == 1:
                if direction == 1:
                    GPIO.output(D[(i + j) % 8],1)
                else:
                    GPIO.output(D[(i - j) % 8],1)
        time.sleep(0.5)            
        GPIO.output(D,0)
        
        j = j + 1
        
            
def shm(period,frec):
    while True:
        
        GPIO.PWM(D[0],frec)
        time.sleep(period)
        frec = frec * 2



p = GPIO.PWM(12, 50)  # channel=12 frequency=50Hz
p.start(0)
try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
 


#lightUp(5,10)
#blink(1,10,1)
#runningLight(5,0.1)
#runningDark(2,0.1)
#lightNumber(79)
#runningPattern(133, 1)
#shm(1, 5)

#GPIO.output(D,0)
#GPIO.cleanup(D)   