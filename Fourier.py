# サンプリングレート（サンプリング周波数）

import numpy as np
import matplotlib.pyplot as plt

# 量子化（離散化）
f_s = 44100 # サンプリングレート f_s[Hz]
t_fin = 1 # 収録終了時刻 [s]
dt = 1/f_s # サンプリング周期 dt[s]
N = int(f_s * t_fin) # サンプル数 [個]

# 入力信号 y(t)
f0 = 440 # 周波数 f0[Hz]
t = np.arange(0, t_fin, dt) # 離散時間 t[s]
y = np.sin(2*np.pi*f0*t) # y(t) を生成

# y(t)のグラフ
plt.plot(t, y) # y-t グラフのプロット
plt.xlim(0, 10*10**-3) # 横軸に関する描画範囲指定
plt.show()