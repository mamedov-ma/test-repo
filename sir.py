from turtle import shape
import math 
from scipy.optimize import minimize
import circle_fit as cf
import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, fftshift


def LeastSquares(BI, BQ):
    data = np.array([BI, BQ]).T
    B_i, B_q, R, _ = cf.least_squares_circle((data))
    return BI - B_i, BQ - B_q

def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)

def RMSE(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())

def ARCTAN(BI, BQ):
    return np.unwrap(np.arctan2(BI,BQ))

def MDACM(BI, BQ):
    X = np.array([np.sum([(BI[i - 1] * BQ[i] - BI[i] * BQ[i - 1]) for i in range(1, j)]) for j in range(1, len(BI))])
    return np.concatenate(([X[0]], X), axis = 0)

def GSOP(BI, BQ):
    E_BI_BQ = np.corrcoef(BI, BQ)[0][1]
    E_BI = np.corrcoef(BI, BI)[0][1]
    E_BQ = np.corrcoef(BQ - E_BI_BQ * BI / E_BI, BQ - E_BI_BQ * BI / E_BI)[0][1]
    BI_new = BI / np.sqrt(E_BI)
    BQ_new = (BQ - E_BI_BQ * BI / E_BI) / np.sqrt(E_BQ)
    return BI_new, BQ_new
    
def easy_mean(f, s_k = 0.2, max_k = 0.9, d = 0.001):
    if not hasattr(easy_mean, "fit"):
        easy_mean.fit = f
    k = s_k if (abs(f - easy_mean.fit) < d) else max_k
    easy_mean.fit += (f - easy_mean.fit) * k
    return easy_mean.fit

def Precondition(BI, BQ, batch_size, window_size):
    #BI = np.array([easy_mean(i) for i in BI])
    #BQ = np.array([easy_mean(i) for i in BQ])
    BI, BQ = GSOP(BI, BQ)
    BI_Preconditioned, BQ_Preconditioned = LeastSquares(BI, BQ)
    return BI_Preconditioned, BQ_Preconditioned



L = 1000
sf = 100
t = np.linspace(0, L/sf, L)
f = 0.3
x = 0.003 * np.sin(2 * np.pi * f * t + 0.3)
lamdba = 3 * 10 ** 8 / (24 * 10 ** 9)
Vq = 2
Vi = 1
BQ = Vq + 0.1 * np.sin(np.pi / 3 * 2 + 4 * np.pi * x / lamdba)
BI = Vi + 0.1 * np.cos(np.pi / 3 * 2 + 4 * np.pi * x / lamdba)
clear_signal = np.unwrap(np.arctan2(BI-Vi,BQ-Vq))
BI_Preconditioned, BI_Preconditioned = Precondition(BI, BQ)
mdacm = MDACM(BI, BQ)
mdacm_ipr = MDACM(BI_Preconditioned, BI_Preconditioned)

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

