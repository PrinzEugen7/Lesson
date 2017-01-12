# -*- coding: utf-8 -*-
def main():
    data = [1,2,3,4,5]          # 配列の生成
    ave = sum(data)/len(data)   # 合計/配列の長さ(データの個数)で平均値を計算
    print(ave)                  # 計算結果を表示

if __name__ == '__main__':
    main()
