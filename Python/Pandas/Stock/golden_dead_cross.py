#-*- coding:utf-8 -*-
import pandas as pd
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
    # 株価の取得(銘柄コード, 開始日, 終了日)
    code = 8704
    data = get_stock(code, '2016-1-1', '2016-12-31')

    # データフレームの作成
    df = pd.DataFrame({'始値':data[1], '終値':data[2], '高値':data[3], '安値':data[4]}, index = data[0])
    
    # 移動平均線の計算
    ma_25d = df['終値'].rolling(window=25).mean()
    ma_75d = df['終値'].rolling(window=75).mean()
    # 移動平均のクロス確認
    cross  = ma_25d > ma_75d
    golden = (cross != cross.shift(1)) & (cross == True)
    dead   = (cross != cross.shift(1)) & (cross == False)
    
    index_g = [i for i, x in enumerate(golden) if x == 1]
    index_d = [i for i, x in enumerate(dead) if x == -1]
    print(index_g)
    # クロスのラベルとデータを追加(GC:1, DC:-1, 何もなし:0)
    df['クロス'] = [x+y*-1 for x,y in zip(golden, dead)]
    #df[col_name] = np.append(np.array([0] * (long_day+3)), df[col_name][long_day+3:])
    print(df)
    # グラフにプロット
    ax = df['終値'].plot(color="blue", label="Close")
    ma_25d.columns = ["MA 25d"]
    ma_25d.plot(ax=ax, ls="--", color="red", label="MA 25d")
    ma_75d.columns = ["MA 75d"]
    ma_75d.plot(ax=ax, ls="--", color="green", label="MA 75d")
    ax.grid()
    ax.legend()

    
if __name__ == "__main__":
    main()
