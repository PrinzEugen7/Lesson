#-*- coding:utf-8 -*-
from coincheck import market
    
def main():
    # ビットコインのデータ取得
    ma = market.Market()
    data = ma.ticker()
    # データを表示
    print('ask:', data['ask'])
    print('low:', data['low'])
    print('high:', data['high'])
    print('bid:', data['bid'])
    print('last:', data['last'])
    print('timestamp:', data['timestamp'])
    print('volume:', data['volume'])
             
if __name__ == "__main__":
    main()
