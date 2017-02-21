# -*- coding: utf-8 -*-
import pandas as pd

def main():
    data ={
        'miho'  : [158, 82, 56, 84],
        'yukari': [157, 78, 58, 83],
        'saori' : [157, 85, 60, 86]
    }
    # 日時のインデックス作成
    date = pd.date_range("20170201", periods=4)
    df = pd.DataFrame(data,index = date)
    # 表示
    print(df)

if __name__ == '__main__':
    main()
