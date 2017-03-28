#-*- coding:utf-8 -*-
import jsm
import datetime
import numpy as np
import matplotlib.pyplot as plt

# 株価のデータ取得（銘柄コード, 開始日, 終了日）
def get_stock(code, start_date, end_date):
    # 期間設定
    year, month, day = start_date.split("-")
    start = datetime.date(int(year), int(month), int(day))
    year, month, day = end_date.split("-") 
    end = datetime.date(int(year), int(month), int(day))
    # 株価データ取得
    q = jsm.Quotes()
    target = q.get_historical_prices(code, jsm.DAILY, start_date = start, end_date = end)
    # 項目ごとにリストに格納して返す
    date = [data.date for data in target]
    open = [data.open for data in target]
    close = [data.close for data in target]
    high = [data.high for data in target]
    low = [data.low for data in target]

    return [date, open, close, high, low]


# 移動平均線の計算(データ, 日数)
def move_average(data, day):
    return np.convolve(data, np.ones(day)/float(day), 'valid')

# ゴールデンクロス・デッドクロスの探索
def search_cross(f1, f2, i=0):
    golden = []
    dead = []
    df = f1 - f2
    for i in range( len(df)-1 ):        
        # 短い方(f1)が長い方(f2)を上に突き抜けた時の座標取得
        if(df[i] < 0 and df[i+1] > 0):
            golden.append([i, f1[i]])
        # 短い方(f1)が長い方(f2)を下に突き抜けた時の座標取得
        if(df[i] > 0 and df[i+1] < 0):
            dead.append([i, f1[i]])
            
    return np.array(golden), np.array(dead)

    
def main():
    # 株価の取得(銘柄コード, 開始日, 終了日)
    code = 8704
    data15 = get_stock(code, '2015-1-1', '2015-12-31')
    data16 = get_stock(code, '2016-1-5', '2016-12-31')
    data15 = np.array(data15)
    data16 = np.array(data16)
    # 終値だけを日付を古い順に並び替えて抽出
    f15, f16 = data15[2,::-1], data16[2, ::-1] 
    # 移動平均線(25日線)の計算
    day = 25    # 日数
    data = np.r_[f15[len(f15)-day+1:len(f15)], f16]    #　2015年の終値の一部と2016年の終値を結合
    ma_25d = move_average(data, day)

    # 移動平均線(75日線)の計算
    day = 75    # 日数
    data = np.r_[f15[len(f15)-day+1:len(f15)], f16]    #　2015年の終値の一部と2016年の終値を結合
    ma_75d = move_average(data, day)
    
    # ゴールデンクロスとデッドクロスの探索
    gc, dc = search_cross(ma_25d, ma_75d)

    # グラフにプロット
    plt.plot(f16,  label="f")
    plt.plot(ma_25d, "--", color="r", label="MA 25d")
    plt.plot(ma_75d, "--", color="g", label="MA 75d")    
    plt.plot(gc[:,0],gc[:,1],"o", ms=10, label="Golden Cross")      
    plt.plot(dc[:,0],dc[:,1],"o", ms=10, label="Dead Cross")  
    #　ラベル軸
    plt.xlabel("Day")
    plt.ylabel("f")
    # 凡例
    plt.legend(bbox_to_anchor=(1.01,1), loc=2, borderaxespad=0)
    # グリッド
    plt.grid()
    # グラフ表示
    plt.show()

        
if __name__ == "__main__":
    main()

