# -*- coding: utf-8 -*-
import cv2
import numpy as np

def main():
    # 三値化の閾値
    th1, th2 = 60, 150 

    # 入力画像とスクリーントーン画像をグレースケールで取得
    gray = cv2.imread("input.jpg", 0) 
    screen = cv2.imread("screen.jpg", 0)

    # スクリーントーン画像を入力画像と同じ大きさにリサイズ
    screen = cv2.resize(screen,(gray.shape[1],gray.shape[0]))

    # Cannyアルゴリズムで輪郭検出し、色反転
    edge = 255 - cv2.Canny(gray, 80, 120)

    # 三値化
    gray[gray <= th1] = 0
    gray[gray >= th2] = 255
    gray[ np.where((gray > th1) & (gray < th2)) ] = screen[ np.where((gray > th1)&(gray < th2)) ]

    # 三値画像と輪郭画像を合成
    gray = cv2.bitwise_and(gray, edge)

    # 結果を出力
    cv2.imwrite("output.jpg", gray)


if __name__ == '__main__':
    main()
