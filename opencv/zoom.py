# -*- coding:utf-8 -*-
import cv2
import numpy as np


def main():
    # 画像の取得
    im = cv2.imread("fubuki.png")
    # 画像の拡大・縮小
    h = im.shape[0]                     # 画像の高さ
    w = im.shape[1]                     # 画像の幅
    resize1 = cv2.resize(im,(w*2,h*2))  # 画像を2倍に拡大
    resize2 = cv2.resize(im,(w/2,h/2))  # 画像を1/2に縮小
    # 結果表示
    cv2.imshow("Resize1",resize1)
    cv2.imshow("Resize2",resize2)
    cv2.waitKey(0)                  # キー入力待機
    cv2.destroyAllWindows()         # ウィンドウ破棄


if __name__ == "__main__":
    main()
