# -*- coding: utf-8 -*-
import pandas as pd

def main():
    # データフレームの初期化
    df = pd.DataFrame({
    '名前' : ['西住みほ', '秋山優花里', '武部沙織'],
    '身長' : [158, 157, 157]},
    index = ['車長', '装填手', '通信手']
    )
    df2 = df.sort(columns='名前', ascending=False)
    # 表示
    print(df2)

if __name__ == "__main__":
    main()
