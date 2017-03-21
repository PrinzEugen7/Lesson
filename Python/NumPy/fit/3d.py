

# -*- coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

def main():
    # CSVのロード
    data = np.genfromtxt("nikkei16.csv",delimiter=",", skip_header=1, dtype='float')
    
    # 5行目を抽出(日経平均株価の終値)
    f = data[:,4]/1000.0
    
    #　xの値を生成
    x = np.linspace(1, len(f), len(f))
    
    #　フィッティング
    a1, a2, a3, b = np.polyfit(x, f, 3)
    
    # フィッティング関数
    fh = a1 * x**3 + a2 * x**2 + a3 * x + b
    
    # グラフ作成
    plt.figure(1)

    # サンプル(日経平均株価)
    plt.plot(x, f,  label="f")
    plt.plot(x, fh, label="fh")
    #　ラベル軸
    plt.xlabel("Day")
    plt.ylabel("f")
    # 凡例
    plt.legend()
    # グリッド
    plt.grid()
    # グラフ表示
    plt.show()
    
if __name__ == "__main__":
    main()

