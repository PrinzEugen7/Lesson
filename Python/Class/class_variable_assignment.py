# -*- coding: utf-8 -*-

# クラスの定義
class MyClass():
    x = 10

def main():
    # クラス変数に値を代入
    MyClass.x = 20

    # クラス変数の中身を表示
    print(MyClass.x)


if __name__ == "__main__":
    main()
