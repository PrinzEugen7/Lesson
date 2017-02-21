# -*- coding: utf-8 -*-
import pandas as pd

def main():
    # データフレームの初期化
    df = pd.DataFrame({
        'miho'  : [158, 82, 56, 84],
        'yukari': [157, 78, 58, 83],
        'saori' : [157, 85, 60, 86]
    })
    # 表示
    print(df)

if __name__ == "__main__":
    main()
