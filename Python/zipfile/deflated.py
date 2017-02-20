# -*- coding: utf-8 -*-
import zipfile

def main():
    # ZIP圧縮するファイルのリスト
    filelist = ["test.jpg","test.png","test.txt"]
    # ZIP圧縮の設定
    zip1 = zipfile.ZipFile("test.zip", "w", zipfile.ZIP_DEFLATED)
    # ZIP圧縮
    for i, filename in enumerate(filelist):
        zip1.write(filename)

    zip1.close()

if __name__ == "__main__":
    main()
