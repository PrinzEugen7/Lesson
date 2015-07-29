# -*- coding:utf-8 -*-
import cv2
import numpy as np


def main():
    # 画像の取得
    im = cv2.imread("fubuki.png")
    # ガンマ補正
    value = 0.7                     # パラメータ
    im = cv2.pow(im/255.0, value)
    gamma = np.uint8(im*255)
    # 結果表示
    cv2.imshow("Gamma",gamma)
    cv2.waitKey(0)                  # キー入力待機
    cv2.destroyAllWindows()         # ウィンドウ破棄


if __name__ == "__main__":
    main()
