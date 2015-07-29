# -*- coding: utf-8 -*-
import Image
import cv2
import numpy as np
import os.path
import glob

# Raw画像の読み込み
def load_raw(fn, mode, (w, h)):
    # バイナリモードでファイル読み込み
    f = open(fn, "rb")
    # 8bitのRAW画像としてデータ取得
    im = Image.fromstring(mode, (w, h), f.read())
    # pilからopencvにフォーマット変換して返す
    return np.asarray(im)

def main():
    # すべてのraw画像をpng画像に変換
    for fn in glob.glob("*.raw"): # 変換前の拡張子
        file, ext = os.path.splitext(fn)
        im = load_raw(fn, "L", (800, 600))
        cv2.imwrite(file + ".png",im) # 変換後の拡張子

if __name__ == '__main__':
    main()
