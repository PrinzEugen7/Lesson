# -*- coding: utf-8 -*-

# クラスの定義
class MyClass():
    # コンストラクタ
    def __init__(self):
        # インスタンス変数の宣言・初期化
        self.x = 10
        self.y = 20
        self.z = self.x + self.y

def main():
    # インスタンスの生成
    my = MyClass()
    # インスタンス変数の値を取得
    z = my.z 
    # インスタンス変数の中身を表示
    print(z)


if __name__ == "__main__":
    main()
