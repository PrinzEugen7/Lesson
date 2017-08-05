#-*- coding:utf-8 -*-
import cv2
import numpy as np


def equalize_hist(src):

    # 画像の高さ・幅を取得
    h, w = src.shape[0], src.shape[1]
    
    # 全画素数
    s = w * h
    
    # 画素値の最大値
    imax = src.max()
    
    # ヒストグラムの算出
    hist, bins = np.histogram(src.ravel(),256,[0,256])

    # 出力画像用の配列（要素は全て0）
    dst = np.empty((h,w))

    for y in range(0, h):
        for x in range(0, w):
            # ヒストグラム平均化の計算式
            dst[y][x] = np.sum(hist[0: src[y][x]]) * (imax / s)

    return dst


def main():
    # 入力画像を読み込み
    img = cv2.imread("input.jpg")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # 方法1(NumPyで実装)
    dst1 = equalize_hist(gray)

    # 方法2(OpenCVで実装)
    dst2 = cv2.equalizeHist(gray)
    
    # 結果の出力
    cv2.imwrite("output1.jpg", dst1)
    cv2.imwrite("output2.jpg", dst2)


if __name__ == "__main__":
    main()
