# -*- coding: utf-8 -*-
import cv2
import pylab as plt


if __name__ == '__main__':

    # 画像取得
    im = cv2.imread("renge.jpg")

    graph = plt.figure()

    # チャネルB(青)のヒストグラム
    graph.add_subplot(311)
    plt.hist(im[:,:,0].ravel(), 256, range=(0, 255), fc='b')
    plt.xlim(0,255)

    # チャネルG(緑)のヒストグラム
    graph.add_subplot(312)
    plt.hist(im[:,:,1].ravel(), 256, range=(0, 255), fc='g')
    plt.xlim(0,255)

    # チャネルR(赤)のヒストグラム
    graph.add_subplot(313)
    plt.hist(im[:,:,2].ravel(), 256, range=(0, 255), fc='r')
    plt.xlim(0,255)

    # ヒストグラム表示
    plt.show()
