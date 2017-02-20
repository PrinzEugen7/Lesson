# -*- coding: utf-8 -*-
import os

def main():
    # ファイルパス
    path = "D:/img/gochiusa"
    # ファイルパスが存在するかどうかの判定
    if os.path.exists(path):
        print("ファイルパスが存在します")
    else:
        print("ファイルパスが存在しません")


if __name__ == "__main__":
    main()
