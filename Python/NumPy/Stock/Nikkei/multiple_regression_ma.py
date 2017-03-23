# -*- coding: utf-8
import numpy as np

# 移動平均線の計算(データ, 日数)
def move_average(data, day):
    return np.convolve(data, np.ones(day)/float(day), 'valid')

# 重回帰分析（偏回帰係数の計算）
def stat(y, x):

    x = np.vstack([np.ones(x.shape[1]), x]) # 定数項, 説明変数
    return np.linalg.lstsq(x.T, y)[0]       # 偏回帰係数

def main():
     # CSVのロード(2015年と2016年のデータ)
    data15 = np.genfromtxt("nikkei15.csv", delimiter=",", skip_header=1, dtype='float')
    data16 = np.genfromtxt("nikkei16.csv", delimiter=",", skip_header=1, dtype='float')

    # 5列目の終値だけを取り出し
    f15 = data15[:,4]
    f16 = data16[:,4]

    # 移動平均線を計算
    days = [5, 25, 75, 200]
    for day in days:
        data = np.r_[f15[len(f15)-day:len(f15)-1], f16]    #　2015年の終値の一部と2016年の終値を結合
        if(day == days[0]):
            ma =  move_average(data, day)
        ma =  np.vstack([ma, move_average(data, day)])

    # 説明変数(前日の移動平均線)    
    x = np.array([ma[0], ma[1], ma[2], ma[3]])

    # 重回帰分析(偏回帰係数の計算)
    b, a1, a2, a3, a4 = stat(f16, x)
    f16h = a1 * ma[0] + a2 * ma[1] + a3 * ma[2] + a4 * ma[3] + b
    
    # グラフにプロット
    plt.plot(f16,  label="f16")
    plt.plot(f16h, label="f16h")  
    
    #　ラベル軸
    plt.xlabel("Day")
    plt.ylabel("f")
    # 凡例
    plt.legend()
    # グリッド
    plt.grid()
    # グラフ表示
    plt.show()
