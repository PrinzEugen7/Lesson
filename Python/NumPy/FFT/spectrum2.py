# -*- coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

def main():
    # CSVのロード
    data = np.genfromtxt("nikkei.csv",delimiter=",", skip_header=1, dtype='float')
    
    # 5行目を抽出(日経平均株価の終値)
    f = data[:,4]/1000.0

    # サンプル数
    N = len(f)
    
    # 高速フーリエ変換
    F = np.fft.fft(f)/(N/2)
    
    # 直流成分の振幅を揃える
    F[0] = F[0]/2
    
    # 振幅スペクトル
    amp = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in F]  
    
    # 位相スペクトル
    phase = [np.arctan2(int(c.imag), int(c.real)) for c in F]    
    
    # 周波数軸の値を計算 
    freq = np.fft.fftfreq(len(f))     
    
    # グラフ作成
    plt.figure(1)
    
    # サンプル(日経平均株価)
    plt.subplot(221)
    plt.plot(f)
    plt.xlabel("Time")
    plt.ylabel("f")

    # 振幅
    plt.subplot(222)
    plt.plot(freq, amp)

    plt.xlabel("Fequency")    
    plt.ylabel("Amplitude")
    
    # 位相
    plt.subplot(223)
    plt.plot(freq, np.degrees(phase))
    plt.xlabel("Fequency")   
    plt.ylabel("Phase[deg]")
    
    # グラフ表示
    plt.show()
    
if __name__ == "__main__":
    main()
