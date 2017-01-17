# -*- coding: utf-8 -*-

# クラスの定義
class MyClass():
    def __init__(self):
        self.x = 10     # インスタンス変数x
        self.y = 20     # インスタンス変数y
        self.z = self.x + self.y

def main():
    # インスタンスの生成
    my = MyClass()

    # インスタンス変数の中身を表示
    print(my.z)


if __name__ == "__main__":
    main()
