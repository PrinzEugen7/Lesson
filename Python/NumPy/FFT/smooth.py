# -*- coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

def main():
    # CSVのロード
    data = np.genfromtxt("nikkei.csv",delimiter=",", skip_header=1, dtype='float')
    
    # 5行目を抽出(日経平均株価の終値)
    f = data[:,4]/1000.0
    
    # サンプル数, カットオフ周波数    
    N = len(f)

    fc = 0.1

    # 高速フーリエ変換
    F = np.fft.fft(f)/(N/2)
    
    # 周波数軸の値を計算 
    freq = np.fft.fftfreq(len(f))
    # 直流成分の振幅を揃える
    F[0] = F[0]/2
    
    # ローパス処理
    F[(freq > fc)] = 0
    F[(freq < 0)] = 0
    
    # 高速逆フーリエ変換
    f2 = np.fft.ifft(F)*(2*N/2)
 
    # グラフ作成
    plt.figure(1)
    
    # サンプル(日経平均株価)
    plt.subplot(221)
    plt.plot(f)
    plt.xlabel("Time")
    plt.ylabel("f")

    # 平滑化データ
    plt.subplot(222)
    plt.plot(f2)
    plt.xlabel("Time")
    plt.ylabel("f2")
    
    # グラフ表示
    plt.show()
    
if __name__ == "__main__":
    main()
