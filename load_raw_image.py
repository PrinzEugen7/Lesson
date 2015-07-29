# -*- coding: utf-8 -*-
import Image
import cv2
import numpy as np

# Raw画像の読み込み
def load_raw(fn, mode, (w, h)):
    # バイナリモードでファイル読み込み
    f = open(fn, "rb")
    # 8bitのRAW画像としてデータ取得
    im = Image.fromstring(mode, (w, h), f.read())
    # pilからopencvにフォーマット変換して返す
    return np.asarray(im)

def main():
    im = load_raw("test.raw", "L", (640, 480))
    # 画像表示
    cv2.imshow("Show Raw Image",im)
    cv2.imwrite("test.jpg",im)
    # キー入力待機
    cv2.waitKey(0)
    # ウィンドウ破棄
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
