from os.path import dirname, join as pjoin
from scipy.io import wavfile
import scipy.io
import matplotlib.pyplot as plt
import numpy as np
import csv
import xlsxwriter



wav_fname = pjoin('C:\miner\git repository\DAC', 'LS110034.wav')
samplerate, data = wavfile.read(wav_fname)
print(f"number of channels = {data.shape[1]}")
length = data.shape[0] / samplerate
print(f"length = {length}s")
print(data.shape[0])
print(samplerate)
#print(data)

a = round(data.shape[0] / 2)

workbook = xlsxwriter.Workbook('C:\miner\git repository\DAC\sound.xlsx')
worksheet = workbook.add_worksheet()
for i in range(0, a):
    worksheet.write(i, 0, data[i, 0])
    worksheet.write(i, 1, data[i, 1])
    worksheet.write(i, 2, np.around(i / samplerate, 8))

workbook.close() 



time = np.linspace(0, length, data.shape[0])
plt.plot(time, data[:, 0], label="Left channel")
plt.plot(time, data[:, 1], label="Right channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()



