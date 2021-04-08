import numpy as np
import matplotlib.pyplot as plt
import time
import math
import csv
import xlsxwriter


def sin(time_, samplingFrequence, frequence):  
   
    Time = np.arange(0, time_, samplingFrequence)
    amplitude = (255 * np.sin(Time * 2 * math.pi * frequence))
    amplitude = np.around(amplitude)
    plt.plot(Time, amplitude)
    plt.title('sin')
    plt.xlabel('time')
    plt.ylabel('sin(time)')
    plt.minorticks_on()
    amplitude = abs(amplitude)
    #print(amplitude)
    #print(Time)
    

    workbook = xlsxwriter.Workbook('C:\miner\git repository\DAC\DATA.xlsx')
    worksheet = workbook.add_worksheet()
    a = round(time_ / samplingFrequence)
    for i in range(0,a):
        worksheet.write(i, 0, amplitude[i])
        print(amplitude[i])

    workbook.close()
    
    
    
    
    #fl = open('data.csv', 'w')
    #writer = csv.writer(fl)
    #for values in amplitude:
    #    writer.writerow(values)
    #fl.close()
    
    
    #plt.show()
    
    
    
    
sin(10, 0.001, 10) 
    

