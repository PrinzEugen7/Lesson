# -*- coding: utf-8 -*-

# クラスの定義
class MyClass():
    # コンストラクタ(初期化メソッド)
    def __init__(self, text):
        self.text = text

def main():
    # コンストラクタでインストラクタ変数を初期化
    my = MyClass("Nyan Pass!")
    # インストラクタ変数を表示
    print(my.text)


if __name__ == "__main__":
    main()
