# -*- coding: utf-8 -*-
import cv2
import pylab as plt

if __name__ == '__main__':

    # 画像をグレースケールで取得
    im = cv2.imread("lena.jpg",0)

    # ヒストグラムを求める
    hist = cv2.calcHist([im],[0],None,[256],[0,256])

    # ヒストグラム表示
    plt.plot(hist)
    plt.xlim(0,255)
    plt.show()
