# -*- coding: utf-8 -*-
import os

def main():
    # パス
    path = "D:/img/gochiusa"
    # ファイルパスが存在するかどうかの判定
    if os.path.isfile(path):
        print("パスはファイルです。")
    else:
        print("パスはファイルでないです。")


if __name__ == "__main__":
    main()
