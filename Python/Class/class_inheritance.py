# -*- coding: utf-8 -*-

# スーパークラスの定義
class MyClass1:
    # コンストラクタ(初期化メソッド)
    def __init__(self, x, y):
        self.x = x
        self.y = y


# サブクラスの定義
class SubClass(MyClass1):
    # メソッド(追加分)
    def dot(self):
        self.z = self.x * self.y
        return self.z

def main():
    # サブクラスのインストラクタを生成
    mysub = SubClass(10, 20)

    print( mysub.dot() )


if __name__ == "__main__":
    main()
