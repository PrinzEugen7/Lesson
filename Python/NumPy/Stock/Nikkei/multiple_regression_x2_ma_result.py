# -*- coding: utf-8
import numpy as np

# 移動平均線の計算(データ, 日数)
def move_average(data, day):
    return np.convolve(data, np.ones(day)/float(day), 'valid')

# 重回帰分析（偏回帰係数の計算）
def stat(y, x):
    x = np.vstack([np.ones(x.shape[1]), x]) # 定数項, 説明変数
    return np.linalg.lstsq(x.T, y)[0]       # 偏回帰係数

# 前日から上昇・下落のチェック
def ud(f):
    # 勾配を計算
    df = np.gradient(f)
    df[df > 0] = 1
    df[df == 0] = 0
    df[df < 0] = -1

    return df
    
def main():
    # CSVのロード(2014年～2016年のデータ)
    data14 = np.genfromtxt("nikkei14.csv", delimiter=",", skip_header=1, dtype='float')
    data15 = np.genfromtxt("nikkei15.csv", delimiter=",", skip_header=1, dtype='float')
    data16 = np.genfromtxt("nikkei16.csv", delimiter=",", skip_header=1, dtype='float')

    # 5列目の終値だけを古い順に並び替えて取り出し
    f14, f15, f16 = data14[:,4], data15[:,4], data16[:,4]
    f14, f15, f16 = f14[::-1], f15[::-1], f16[::-1]

    # 2015年分と2016年分の移動平均線を計算
    days = [5, 25, 75, 200]
    for day in days:
        data15 = np.r_[f14[len(f14)-day:len(f14)-1], f15]    #　2015年の終値の一部と2016年の終値を結合
        data16 = np.r_[f15[len(f15)-day:len(f15)-1], f16]    #　2015年の終値の一部と2016年の終値を結合
        if(day == days[0]):
            ma15 =  move_average(data15, day)
            ma16 =  move_average(data16, day)
        ma15 =  np.vstack([ma15, move_average(data15, day)])
        ma16 =  np.vstack([ma16, move_average(data16, day)])

    # 説明変数(2015年の移動平均線(前日))    
    x = np.array([ma15[0], ma15[1]])

    # 重回帰分析(偏回帰係数の計算)
    b, a1, a2 = stat(f15, x)
    
    # (前日の移動平均線)+(2015年データで求めた偏回帰係数)→2016年の株価を予測
    f16h = a1 * ma16[0] + a2 * ma16[1] + b
    
    df16 = ud(f16)
    df16h = ud(f16h)
    
    # 差分を計算
    result = df16 - df16h
    
    # 差分が0(当たり)の個数を計算
    hit = len(result) - np.count_nonzero(result)
    
    # 当たりの確率をパーセント表示
    score = 100*hit/len(result)
    print(round(score, 3), "[%]")


if __name__ == "__main__":
    main()
