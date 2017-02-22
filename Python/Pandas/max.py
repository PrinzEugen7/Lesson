# -*- coding: utf-8 -*-
import pandas as pd

def main():
    # CSVファイルの読み込み
    df = pd.read_csv("artoria.csv", index_col=0)
    # 計算
    dfmax = df['ATK'].max()
    # 表示
    print("max:",dfmax)


if __name__ == '__main__':
    main()
