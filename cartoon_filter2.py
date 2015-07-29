# -*- coding: utf-8 -*-
import numpy as np
import cv2

def main():
    im = cv2.imread("test.jpg")                     # 画像の取得
    n = 50
    im = (im/n)*n                                   # 減色処理
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)     # 画像のグレースケール変換
    edge = cv2.Canny(gray, 50, 150)                 # 輪郭線を検出
    edge = cv2.cvtColor(edge,cv2.COLOR_GRAY2BGR)	# 輪郭画像をRGBに変換
    im = im - edge                                  # 輪郭線を除去
    cv2.imshow("Result",im)                         # 結果を表示
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
