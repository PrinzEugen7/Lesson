# -*- coding: utf-8 -*-
import pandas as pd

def main():
    # リスト生成
    name = ['西住みほ', '秋山優花里', '武部沙織']
    height = [158, 157, 157]
    position = ['車長', '装填手', '通信手']
    
    # リスト→データフレーム
    df = pd.DataFrame({'名前' : name, '身長' : height}, index = position)

    # データフレーム表示
    print(df)
    
    '''
        　　　　名前   身長
    車長    西住みほ  158
    装填手  秋山優花里  157
    通信手   武部沙織  157
    '''
    indexes = [0, 1]
    columns = [0]
    
    # ラベル（列）を抽出
    df2 = df.iloc[indexes, columns]
    # 抽出したデータフレームを表示
    print(df2)
    '''
              名前
    車長      西住みほ
    装填手    秋山優花里
    '''
    
if __name__ == "__main__":
    main()
