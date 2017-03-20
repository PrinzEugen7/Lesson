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
    F = np.fft.fft(f)
    
    # 高速逆フーリエ変換
    f2 = np.fft.ifft(F)
 
    # グラフ作成
    plt.figure(1)
    
    # サンプル(日経平均株価)
    plt.subplot(221)
    plt.plot(f)
    plt.xlabel("Time")
    plt.ylabel("f")

    # 振幅
    plt.subplot(222)
    plt.plot(f2)
    plt.xlabel("Time")
    plt.ylabel("f2")
    
    # グラフ表示
    plt.show()
    
if __name__ == "__main__":
    main()
