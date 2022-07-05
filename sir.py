from struct import unpack
from tkinter import ARC
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift

L = 1000
sf = 100
t = np.linspace(0, L/sf, L)
f = 0.3
x = 0.003 * np.sin(2 * np.pi * f * t + 0.3)
lamdba = 3 * 10 ** 8 / (24 * 10 ** 9)
Vq = 2
Vi = 1
a_k = 0.6
b_k = 1
BQ = Vq + 0.1 * np.sin(np.pi / 3 * 2 + 4 * np.pi * x / lamdba)
BI = Vi + 0.1 * np.cos(np.pi / 3 * 2 + 4 * np.pi * x / lamdba)
clear_signal = np.unwrap(np.arctan2(BI-Vi,BQ-Vq))


def EVM(BI, BQ):
    V_ref = 1
    V_mean = np.array([abs(BI - 1), abs(BQ - 2)])
    V_err = V_mean - V_ref
    return 10 * np.sum([np.log10((np.sqrt(V_err[0][i] ** 2 + V_err[1][i] ** 2)) / (V_ref)) for i in range(0, L)]) / L

def RMSE(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

def ARCTAN(BI, BQ):
    return np.unwrap(np.arctan2(BI,BQ))

def DPoD(BI, BQ):
    return np.concatenate(([BQ[0]], [BQ[i] * ((1 - a_k * t[i] ** (-1)) / (1 - b_k * t[i] ** (-1))) for i in range(1, L)]), axis = 0), np.concatenate(([BI[0]], [BI[i] * ((1 - a_k * t[i] ** (-1)) / (1 - b_k * t[i] ** (-1))) for i in range(1, L)]), axis = 0)

def BASS(BI, BQ):
    return BI, BQ

def MDACM(BI, BQ):
    X = lamdba / (4 * np.pi) * np.array([np.sum([BI[i - 1] * BQ[i] - BI[i] * BQ[i - 1] for i in range(1, j)]) for j in range(1, 1000)])
    return np.concatenate(([X[0]], X), axis = 0)






'''
plt.close('all')
pn = 0
plt.figure(pn)
plt. subplot(121)
plt.title(label = 'EVM = ' + str(EVM(BI, BQ)))
plt.plot(BI, BQ, 'o', color='red')
plt.subplot(122)
plt.title(label = 'EVM = ' + str(EVM(BI_out, BQ_out)))
plt.plot(BI_out, BQ_out, 'o', color='red')

pn +=1
plt. figure(pn)
plt.subplot(121)
plt.title(label = 'in')
plt.plot(t, np.unwrap(np.arctan2(BI,BQ)), color='red')
plt. subplot(122)
plt.title(label ='out')
plt.plot(t, np.unwrap(np.arctan2(BI_out,BQ_out)), color='red')

pn +=1
plt.figure(pn)
plt. subplot(121)
plt.title(label = 'in')
plt.plot(t, np.unwrap(np.arctan2(BI-Vi,BQ-Vq)), color='blue')
plt. subplot(122)
plt.title(label ='out')
plt.plot(t, np.unwrap(np.arctan2(BI_out-Vi,BQ_out-Vq)), color='blue')

pn +=1
plt.figure(pn)
y = np.unwrap(np.arctan2(BI, BQ))
yf = fft(y)
xf = fftfreq(L, 1/sf)
xf = fftshift(xf)
yplot = fftshift(yf)
plt. subplot(121)
plt.title(label = 'in')
plt.plot(xf, 1.0 / L * np.abs(yplot))

y_out = np.unwrap(np.arctan2(BI_out, BQ_out))
yf_out = fft(y_out)
xf_out = fftfreq(L, 1/sf)
xf_out = fftshift(xf_out)
yplot_out = fftshift(yf_out)
plt. subplot(122)
plt.title(label = 'in')
plt.plot(xf_out, 1.0 / L * np.abs(yplot_out))


plt.show()
a = np.array([3, 1], [2, 2])
w, v = np.linalg.eig(a)

print(w)
print(v)

'''

plt.close('all')
pn = 0
plt.figure(pn)
plt. subplot(131)
plt.title(label = 'RMSE = ' + str(RMSE(ARCTAN(BI-Vi,BQ-Vq), clear_signal)))
plt.plot(t, ARCTAN(BI-Vi,BQ-Vq), color='blue')
plt.subplot(132)
plt.title(label = 'RMSE = ' + str(RMSE(ARCTAN(BI, BQ), clear_signal)))
plt.plot(t, ARCTAN(BI, BQ), color='red')
plt.subplot(133)
plt.title(label = 'RMSE = ' + str(RMSE(MDACM(BI, BQ), clear_signal)))
plt.plot(t, MDACM(BI, BQ), color = 'red')
plt.show()

