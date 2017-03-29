#-*- coding:utf-8 -*-

def main():
    # リスト生成
    data = [1,2,3,4,5,4,3,2,1]
    # 値3をもつ全てのインデックス
    indexes = [i for i, e in enumerate(data) if e == 3]
    # 結果表示
    print(indexes) # [2, 6]
    
if __name__ == "__main__":
    main()
