#-*- coding:utf-8 -*-
import sys
 
def main():
    # リスト宣言
    array = ["沖田", "武蔵", "モードレッド"]
 
    # インデックスと要素を取り出し
    for i, e in enumerate(array):
        print("要素番号:", i, ", 値:", e)
 
if __name__ == "__main__":
    main()
