# 波のグラフを周波数のグラフに（フーリエ変換）

import numpy as np
import matplotlib.pyplot as plt

f_s = 44100 # サンプリングレート f_s[Hz]
t_fin = 1 # 収録終了時刻 [s]
dt = 1/f_s # サンプリング周期 dt[s]
N = int(f_s * t_fin) # サンプル数 [個]

f0 = 440 # 周波数 f0[Hz]
t = np.arange(0, t_fin, dt) # 離散時間 t[s]
y = np.sin(2*np.pi*f0*t) # y(t) を生成

# FFT: tの関数をfの関数にする
y_fft = np.fft.fft(y) # 離散フーリエ変換
freq = np.fft.fftfreq(N, d=dt) # 周波数を割り当てる
Amp = abs(y_fft/(N/2)) # 音の大きさ（振り幅の大きさ）

plt.plot(freq[1:int(N/2)], Amp[1:int(N/2)])
plt.xscale("log") # 横軸を対数軸にセット
plt.show()