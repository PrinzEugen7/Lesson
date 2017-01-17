# -*- coding: utf-8 -*-

# クラスの定義
class MyClass():
    # コンストラクタ(インスタンス生成時に自動で呼び出される)
    def __init__(self, x, y): # 初期化
        # インスタンス変数の宣言・初期化
        self.x = x
        self.y = y
        self.z = self.x + self.y

def main():
    # インスタンスの生成(同時にインスタンス変数を初期化)
    my = MyClass(10, 20)

    # インスタンス変数の中身を表示
    print(my.z)


if __name__ == "__main__":
    main()
