# -*- coding: utf-8 -*-
import cv2
import numpy as np

def main():
    th1, th2 = 60, 160                      # 3値化の閾値
    gray = cv2.imread("test.png",0)         # 入力画像をグレースケールで取得
    screen = cv2.imread("screen.png",0)     # スクリーントーンの取得
    screen = cv2.resize(screen,(gray.shape[1],gray.shape[0]))   # スクリーントーン画像を入力画像と同じ大きさにリサイズ
    # エッジ検出と色反転
    edge = 255 - cv2.Canny(gray, 80, 120)

    # 画像の3値化
    gray[gray <= th1] = 0
    gray[gray >= th2] = 255
    gray[ np.where((gray > th1)&(gray < th2)) ] = screen[ np.where((gray > th1)&(gray < th2)) ]

    # 3値画像とエッジ画像を合わせる
    gray = cv2.bitwise_and(gray, edge)

    cv2.imshow("Manga",gray)                # 結果を表示
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
