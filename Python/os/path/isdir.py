# -*- coding: utf-8 -*-
import os

def main():
    # パス
    path = "D:/img/gochiusa"
    # ファイルパスが存在するかどうかの判定
    if os.path.isdir(path):
        print("パスはディレクトリです。")
    else:
        print("パスはディレクトリでないです。")


if __name__ == "__main__":
    main()
