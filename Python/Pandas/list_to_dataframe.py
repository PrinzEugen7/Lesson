#-*- coding:utf-8 -*-
import pandas as pd

    
def main():
    # リスト生成
    name = ['西住みほ', '秋山優花里', '武部沙織']
    height = [158, 157, 157]
    position = ['車長', '装填手', '通信手']
    
    # リスト→データフレーム
    df = pd.DataFrame({'名前' : name, '身長' : height}, index = position)
    
    # 表示
    print(df)

        
if __name__ == "__main__":
    main()
