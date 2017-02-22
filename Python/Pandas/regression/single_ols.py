# -*- coding: utf-8 -*-
import pandas as pd

def main():
    # CSVファイルの読み込み
    df = pd.read_csv("artoria.csv", index_col=0)
    # 説明変数
    x = df['ATK'].values
    # 目的変数
    y = df['レアリティ'].values
    model = pd.ols(y=y, x=x, intercept = True)
    # 表示
    print(model)


if __name__ == '__main__':
    main()
