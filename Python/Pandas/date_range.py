# -*- coding: utf-8 -*-
import pandas as pd

def main():
    # 日時のインデックス作成
    date = pd.date_range("20170201", periods=21)
    # 表示
    print(date)

if __name__ == '__main__':
    main()
