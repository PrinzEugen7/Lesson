# -*- coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

def main():
    # CSVのロード
    data = np.genfromtxt("nikkei.csv",delimiter=",", skip_header=1, dtype='float')
    # 5行目を抽出(日経平均株価の終値)
    f = data[:,4]/1000

    # 高速フーリエ変換
    F = np.fft.fft(f)

    # グラフ作成
    plt.figure(1)
    
    # サンプル(日経平均株価)
    plt.subplot(221)
    plt.plot(f)
    plt.xlabel("Time")
    plt.ylabel("f")

    # 振幅
    plt.subplot(222)
    plt.plot(np.abs(F))
    plt.ylim(0, 20)
    plt.xlabel("Data number")    
    plt.ylabel("Amplitude")
    
    # 位相
    plt.subplot(223)
    plt.plot(np.degrees(np.angle(F)))
    plt.xlabel("Data number")
    plt.ylabel("Phase[deg]")
    
    # グラフ表示
    plt.show()
    
if __name__ == "__main__":
    main()
