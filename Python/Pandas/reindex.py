# -*- coding: utf-8 -*-
import pandas as pd

def main():
    # CSVファイルの読み込み
    df = pd.read_csv("artoria.csv", index_col=0)
    # 処理
    df2 = df.reindex(['アルトリア(リリイ)','アルトリア(オルタ)','アルトリア(水着)'])
    # 表示
    print(df2)


if __name__ == '__main__':
    main()
