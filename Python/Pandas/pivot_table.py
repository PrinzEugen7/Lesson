# -*- coding: utf-8 -*-
import pandas as pd

def main():
    # データフレームの初期化
    df = pd.DataFrame({
    '名前' : ['西住みほ', '秋山優花里', '武部沙織', '五十鈴華', '冷泉麻子'],
    '身長' : [158, 157, 157, 163, 145]},
    index = ['車長', '装填手', '通信手', '砲手', '操縦手']
    )
    # データ取り出し
    df2 = pd.pivot_table(df, values='砲手', index=['車長', '装填手'], columns=['通信手'])
    print(df2)

if __name__ == "__main__":
    main()
