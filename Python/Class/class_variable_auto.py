# -*- coding: utf-8 -*-

# クラスの定義
class MyClass():
    x = 10

def main():
    # クラス変数を追加
    MyClass.y = 20

    # クラス変数の中身を表示
    print(MyClass.y)


if __name__ == "__main__":
    main()
