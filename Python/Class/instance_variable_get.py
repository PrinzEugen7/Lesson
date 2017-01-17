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

    # インスタンス変数の中身を表示
    print(my.z)


if __name__ == "__main__":
    main()
