# -*- coding: utf-8 -*-

# クラスの定義
class MyClass():
    n = 0
    # コンストラクタ(初期化メソッド)
    def __init__(self):
        MyClass.n += 1

def main():
    # インスタンスを2つ生成
    my1 = MyClass()
    my2 = MyClass()
    # インストラクタ変数を表示
    print(MyClass.n)
