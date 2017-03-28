# -*- coding: utf-8
import numpy as np

# 移動平均線の計算(データ, 日数)
def move_average(data, day):
    return np.convolve(data, np.ones(day)/float(day), 'valid')
    
def main():
     # CSVのロード(2015年と2016年のデータ)
    data15 = np.genfromtxt("nikkei15.csv", delimiter=",", skip_header=1, dtype='float')
    data16 = np.genfromtxt("nikkei16.csv", delimiter=",", skip_header=1, dtype='float')

    # 5列目の終値だけを日付古い順に並び替えて取り出し
    f15, f16 = data15[:,4], data16[:,4]
    f15, f16 = f15[::-1], f16[::-1]

    # 移動平均線を計算
    days = [5, 25, 75, 200]
    for day in days:
        data = np.r_[f15[len(f15)-day+1:len(f15)], f16]    #　2015年の終値の一部と2016年の終値を結合
        if(day == days[0]):
            ma =  move_average(data, day)
        ma =  np.vstack([ma, move_average(data, day)])

    # データ保存
    np.savetxt('ma16.csv', ma.T, delimiter=",")


    
if __name__ == "__main__":
    main()
