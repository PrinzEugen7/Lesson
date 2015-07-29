# -*- coding: utf-8 -*-
import cv2
import numpy as np
import pylab as plt

# ヒストグラムの計算
def calc_hist(im):

    hist = [0]*256
    h = im.shape[0] # 画像の高さ
    w = im.shape[1] # 画像の幅

    for x in range(w):
        for y in range(h):
            # その画素値のヒストグラムの値を１増加
            hist[im[y,x]] += 1

    return hist

if __name__ == '__main__':

    # 画像取得
    im = cv2.imread("renge.jpg",0)

    # ヒストグラムを計算
    hist = calc_hist(im)

    plt.rcParams["font.size"] = 20
    plt.subplot(2,2,1),plt.imshow(im,"gray")
    plt.title("Input Image")
    plt.subplot(2,2,2),plt.plot(hist,"gray")
    plt.title("Equalization Histogram")
    plt.show()
