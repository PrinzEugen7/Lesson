# -*- coding: utf-8 -*-

# クラスの定義
class MyClass():
    # メソッド
    def calc(self, x, y):
        self.z = x + y

def main():
    # インスタンスを生成
    my = MyClass()
    # メソッドcalcに(x=10, y=20)を渡す
    my.calc(10, 20)
    # インストラクタ変数zを表示
    print(my.z)


if __name__ == "__main__":
    main()
