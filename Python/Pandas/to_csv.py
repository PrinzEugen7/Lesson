# -*- coding: utf-8 -*-
import pandas as pd

def main():
    # データフレームの初期化
    df = pd.DataFrame({
    '名前' : ['西住みほ', '秋山優花里', '武部沙織', '五十鈴華', '冷泉麻子'],
    '身長' : [158, 157, 157, 163, 145]},
    index = ['車長', '装填手', '通信手', '砲手', '操縦手']
    )
    # ファイル出力
    df.to_csv("anko.csv")


if __name__ == '__main__':
    main()
