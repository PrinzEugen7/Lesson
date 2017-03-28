# -*- coding: utf-8
import numpy as np

# 回帰分析(x, y)
def fitting(x, f):
    #　xの値を生成
    x = np.linspace(1, len(f), len(f))
    
    #　フィッティング
    a1, a2, a3, b = np.polyfit(x, f, 3)
    
    # フィッティング関数
    fh = a1 * x**3 + a2 * x**2 + a3 * x + b

    # 勾配を計算
    dfh = np.gradient(fh)

    # 3値化(前日の終値よりプラス:1, 変化なし:0, マイナス:-1)
    dfh[dfh > 0] = 1
    dfh[dfh == 0] = 0
    dfh[dfh < 0] = -1

    return fh, dfh
    
def main():
     # CSVのロード(2015年と2016年のデータ)
    data15 = np.genfromtxt("nikkei15.csv", delimiter=",", skip_header=1, dtype='float')
    data16 = np.genfromtxt("nikkei16.csv", delimiter=",", skip_header=1, dtype='float')
    
    # 5行目を抽出(日経平均株価の終値を古い順に並び替え)
    f15, f16 = data15[:,4]/1000.0, data16[:,4]/1000.0
    f15, f16 = f15[::-1], f16[::-1]
    #　xの値を生成
    x15 = np.linspace(1, len(f15), len(f15))
    x16 = np.linspace(1, len(f16), len(f16))   
    # 平滑化
    f15, df15 = fitting(x15, f15)
    f16, df16 = fitting(x16, f16)
    
    # 差分を計算
    result = df15 - df16
    
    # 差分が0(当たり)の個数を計算
    hit = len(result) - np.count_nonzero(result)
    
    # 当たりの確率をパーセント表示
    score = 100*hit/len(result)
    print(round(score, 3), "[%]")

if __name__ == "__main__":
    main()
