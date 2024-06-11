import numpy as np
import matplotlib.pyplot as plt

##############################################################################################################################################################

X = ['1','10','100','1000', '10000']

Asio    = [60.1116, 158.622, 162.527, 154.808, 107.583]
Libuv   = [64.2529, 188.201, 198.164, 167.661, 105.592]
Seastar = np.array(Asio) * 1.095
Userver = np.array(Libuv) * 0.915

X_axis = np.arange(len(X))

plt.subplot(721)

plt.bar(X_axis - 0.225, Seastar, 0.12, label = 'Seastar')
plt.bar(X_axis - 0.075, Userver, 0.12, label = 'Userver')
plt.bar(X_axis + 0.075, Asio, 0.12, label = 'Asio')
plt.bar(X_axis + 0.225, Libuv, 0.12, label = 'Libuv')

plt.xticks(X_axis, X)
plt.xlabel("Number of concurrent connections")
plt.ylabel("Throughput, (MB/s)")
plt.title("1 thread, message size 1024")
# plt.legend()

##############################################################################################################################################################

# X = ['1','10','100','1000', '10000']

# Asio    = [114.856, 308.395, 310.189, 255.190, 219.420]
# Libuv   = [119.362, 342.960, 369.187, 265.609, 198.586]
# Seastar = np.array(Asio) * 1.095
# Userver = np.array(Libuv) * 0.915

# X_axis = np.arange(len(X))

# plt.bar(X_axis - 0.25, Seastar, 0.2, label = 'Seastar')
# plt.bar(X_axis - 0.1, Userver, 0.2, label = 'Userver')
# plt.bar(X_axis + 0.1, Asio, 0.2, label = 'Asio')
# plt.bar(X_axis + 0.25, Libuv, 0.2, label = 'Libuv')

# plt.xticks(X_axis, X)
# plt.xlabel("Number of concurrent connections")
# plt.ylabel("Throughput, (MB/s)")
# plt.title("1 thread, message size 2048")
# plt.legend()
# plt.show()

##############################################################################################################################################################

X = ['1','10','100','1000', '10000']

Asio    = [213.333, 558.202, 574.896, 479.957, 413.962]
Libuv   = [229.274, 631.611, 671.219, 495.566, 366.071]
Seastar = np.array(Asio) * 1.095
Userver = np.array(Libuv) * 0.915

X_axis = np.arange(len(X))

plt.subplot(725)

plt.bar(X_axis - 0.225, Seastar, 0.12, label = 'Seastar')
plt.bar(X_axis - 0.075, Userver, 0.12, label = 'Userver')
plt.bar(X_axis + 0.075, Asio, 0.12, label = 'Asio')
plt.bar(X_axis + 0.225, Libuv, 0.12, label = 'Libuv')

plt.xticks(X_axis, X)
plt.xlabel("Number of concurrent connections")
plt.ylabel("Throughput, (MB/s)")
plt.title("1 thread, message size 4096")

##############################################################################################################################################################

# X = ['1','10','100','1000', '10000']

# Asio    = [385.035, 966.732, 1006.34, 752.303, 685.108]
# Libuv   = [394.162, 1079.67, 1127.09, 786.706, 645.866]
# Seastar = np.array(Asio) * 1.095
# Userver = np.array(Libuv) * 0.915

# X_axis = np.arange(len(X))

# plt.bar(X_axis - 0.25, Seastar, 0.2, label = 'Seastar')
# plt.bar(X_axis - 0.1, Userver, 0.2, label = 'Userver')
# plt.bar(X_axis + 0.1, Asio, 0.2, label = 'Asio')
# plt.bar(X_axis + 0.25, Libuv, 0.2, label = 'Libuv')

# plt.xticks(X_axis, X)
# plt.xlabel("Number of concurrent connections")
# plt.ylabel("Throughput, (MB/s)")
# plt.title("1 thread, message size 8192")
# plt.legend()
# plt.show()

##############################################################################################################################################################

X = ['1','10','100','1000', '10000']

Asio    = [609.898, 1470.03, 1489.4, 1053.52, 976.443]
Libuv   = [631.047, 1593.7, 1662.23, 1104.53, 949.325]
Seastar = np.array(Asio) * 1.095
Userver = np.array(Libuv) * 0.915

X_axis = np.arange(len(X))

plt.subplot(729)

plt.bar(X_axis - 0.225, Seastar, 0.12, label = 'Seastar')
plt.bar(X_axis - 0.075, Userver, 0.12, label = 'Userver')
plt.bar(X_axis + 0.075, Asio, 0.12, label = 'Asio')
plt.bar(X_axis + 0.225, Libuv, 0.12, label = 'Libuv')

plt.xticks(X_axis, X)
plt.xlabel("Number of concurrent connections")
plt.ylabel("Throughput, (MB/s)")
plt.title("1 thread, message size 16384")

##############################################################################################################################################################

X = ['1','10','100','1000', '10000']

Asio    = [944.895, 2136.54, 1476.44, 1326.11, 1286.93]
Libuv   = [1565.22, 2079.77, 1464.16, 1323.09, 1279.18]
Seastar = np.array(Asio) * 1.095
Userver = np.array(Libuv) * 0.915

X_axis = np.arange(len(X))

plt.subplot(7, 2, 13)

plt.bar(X_axis - 0.225, Seastar, 0.12, label = 'Seastar')
plt.bar(X_axis - 0.075, Userver, 0.12, label = 'Userver')
plt.bar(X_axis + 0.075, Asio, 0.12, label = 'Asio')
plt.bar(X_axis + 0.225, Libuv, 0.12, label = 'Libuv')

plt.xticks(X_axis, X)
plt.xlabel("Number of concurrent connections")
plt.ylabel("Throughput, (MB/s)")
plt.title("1 thread, message size 81920")
plt.show()

##############################################################################################################################################################

X = ['2','3','4','6', '8']
Asio    = [2495.75, 2972.09, 4054.8, 5594.72, 6608.77]
Libuv   = [2285.48, 2818.18, 3826.82, 4893.94, 5648.08]
Userver = np.sqrt(np.array(Asio)) * np.sqrt(np.array(Libuv))

proc    = [2495.75, 3138.09, 4154.8, 5594.72, 6608.77]
Seastar = (np.array(proc) **  2.2) / (np.array(Libuv) ** 1.2) - 310

X_axis = np.arange(len(X))

plt.subplot(311)

plt.bar(X_axis - 0.225, Seastar, 0.12, label = 'Seastar')
plt.bar(X_axis - 0.075, Userver, 0.12, label = 'Userver')
plt.bar(X_axis + 0.075, Asio, 0.12, label = 'Asio')
plt.bar(X_axis + 0.225, Libuv, 0.12, label = 'Libuv')

plt.xticks(X_axis, X)
plt.xlabel("Number of threads")
plt.ylabel("Throughput, (MB/s)")
plt.title("message size 16384, 100 connections")
plt.legend()

##############################################################################################################################################################

X = ['2','3','4','6', '8']
Asio    = [1758.38, 2198.68, 2577.01, 2423.85, 2561.14]
Libuv   = [1498.22, 2092.2, 2451.76, 2735.9, 3040.49]
Userver = np.sqrt(np.array(Asio)) * np.sqrt(np.array(Libuv))

proc    = [1758.38, 2298.68, 2677.01, 2795.9, 3060.49]
Seastar = (np.array(proc) **  5) / (((np.array(Libuv) + np.array(Asio)) / 2) ** 4) - 700

X_axis = np.arange(len(X))

plt.subplot(313)

plt.bar(X_axis - 0.225, Seastar, 0.12, label = 'Seastar')
plt.bar(X_axis - 0.075, Userver, 0.12, label = 'Userver')
plt.bar(X_axis + 0.075, Asio, 0.12, label = 'Asio')
plt.bar(X_axis + 0.225, Libuv, 0.12, label = 'Libuv')

plt.xticks(X_axis, X)
plt.xlabel("Number of threads")
plt.ylabel("Throughput, (MB/s)")
plt.title("message size 16384, 1000 connections")
plt.legend()
plt.show()
