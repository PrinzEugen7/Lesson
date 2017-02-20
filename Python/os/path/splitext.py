# -*- coding: utf-8 -*-
import os.path

def main():
    # ファイル名
    filename = "heroinex.jpg"
    # ファイル名と拡張子
    fn, ext = os.path.splitext(filename)
    # 結果表示
    print("ファイル名：", fn)
    print("拡張子：", ext)

if __name__ == "__main__":
    main()
