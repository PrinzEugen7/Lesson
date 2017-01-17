# -*- coding: utf-8 -*-

# クラスの定義
class MyClass():
    def __init__(self):
        self.x = 0     # インスタンス変数xへ内部から値を代入
        self.y = 0     # インスタンス変数yへ内部から値を代入
        self.z = self.x + self.y

def main():
    # インスタンスの生成
    my = MyClass()
    # インスタンス変数へ外部から値を代入
    my.x = 10
    my.y = 20
    my.z = my.x + my.y
    # インスタンス変数の中身を表示
    print(my.z)


if __name__ == "__main__":
    main()
