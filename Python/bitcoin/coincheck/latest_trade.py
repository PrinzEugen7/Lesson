#-*- coding:utf-8 -*-
from coincheck import market
    
def main():
    # ビットコインの最新取引履歴を取得
    ma = market.Market()
    data = ma.trades()
    # データを表示
    for e in data:
        for key, value in e.items():
            print(key,':', value)
        print('--------------')
             
if __name__ == "__main__":
    main()

