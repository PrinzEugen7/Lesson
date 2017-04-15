#-*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import jsm
import datetime

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
    # 日付が古い順に並び替えて返す
    return [date[::-1], open[::-1], close[::-1], high[::-1], low[::-1]]
    
def main():
    # 株価の取得(証券コード, 開始日, 終了日)
    data1 = get_stock(1330, '2016-1-1', '2016-12-31')
    data2 = get_stock(7203, '2016-1-1', '2016-12-31')
    
    # データフレームの作成
    df1 = pd.DataFrame({'始値':data1[1], '終値':data1[2], '高値':data1[3], '安値':data1[4]}, index = data1[0])
    df2 = pd.DataFrame({'始値':data2[1], '終値':data2[2], '高値':data2[3], '安値':data2[4]}, index = data2[0])   
    
    # 移動相関の計算
    s1 = df1.asfreq('B')['終値'].pct_change().dropna()
    s2 = df2.asfreq('B')['終値'].pct_change().dropna()
    corr = pd.rolling_corr(s1, s2, 5).dropna()
    
    # 相関の平均値
    print(corr.mean())
    
    # グラフにプロット
    plt.plot(corr)
    plt.grid()
    plt.show()

    
if __name__ == "__main__":
    main()

