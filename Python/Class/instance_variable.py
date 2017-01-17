# -*- coding: utf-8 -*-

# クラスの定義
class MyClass():
    pass

def main():
    # インスタンスの生成
    my = MyClass()

    # インスタンス変数の生成
    my.x = 10
    my.y = 20
    my.z = my.x + my.y

    # インスタンス変数の中身を表示
    print(my.z)


if __name__ == "__main__":
    main()
