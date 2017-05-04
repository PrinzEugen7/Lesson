# -*- coding: utf-8 -*-
import csv
import datetime as dt

# 365日*24時間分の日付を取得
def get_dates():
    date = dt.datetime(2017, 1, 1, 0, 0)
    dates = []
    for i in range(365*24):
        dates.append(date.strftime('%Y-%m-%d %-H:%M'))
        date += dt.timedelta(hours=1)
    return dates

# 2次元リストをCSVファイルに保存
def write_csv(data):
   with open('data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)   

   f.close()
    
def main():
    dates = get_dates()
    data = [dates] # 2次元リストに変換
    data = list(map(list, zip(*data))) # リストの転置
    write_csv(data)
    
if __name__=='__main__':
    main()
