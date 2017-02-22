# -*- coding: utf-8 -*-
import pandas as pd

def main():
    # CSVファイルの読み込み
    df = pd.read_csv("artoria.csv", index_col=0)
    # 計算
    var = df['ATK'].var()
    # 表示
    print("var:",var)


if __name__ == '__main__':
    main()
