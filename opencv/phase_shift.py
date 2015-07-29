# -*- coding: utf-8 -*-
import Image
import cv2
import numpy as np

# Raw画像の読み込み
def load_raw(fn, mode):
    # バイナリモードでファイル読み込み
    f = open(fn, "rb")
    # 8bitのRAW画像としてデータ取得
    im = Image.fromstring(mode, (640, 480), f.read())
    # pilからopencvにフォーマット変換して返す
    return np.asarray(im)

def main():
    # 位相シフト画像4枚を取得
    im0 = load_raw("0.raw", "L")
    im1 = load_raw("1.raw", "L")
    im2 = load_raw("2.raw", "L")
    im3 = load_raw("3.raw", "L")
    # 位相分布の計算
    fi = np.arctan2(im1-im3,im2-im0)

    fi[np.where(fi<0)] += np.pi*2.0
    im = 254*fi/(np.pi*2.0)
    im = np.asarray(im,dtype=np.uint8)
    # 画像表示
    cv2.imshow("Show Image",im)
    # キー入力待機
    cv2.waitKey(0)
    # ウィンドウ破棄
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
