# -*- coding: utf-8 -*-

# クラスの定義
class MyClass():
    @classmethod
    # クラスメソッド
    def calc(self, text):
        print(text)

def main():
    # クラスメソッドの呼び出し
    MyClass.calc("Nyan Pass!")



if __name__ == "__main__":
    main()
