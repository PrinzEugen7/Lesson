#-*- coding:utf-8 -*-
import cv2
import numpy as np


def main():
    # 画像の読み込み(RGB)
    img = cv2.imread("input.png")

    # 三次元配列(カラー)
    img2 = np.array([[[36, 28, 237], [ 76, 177, 34], [204, 72, 63]],
                     [[0, 0 ,0], [255, 255, 255], [195, 195, 195]],
                     [[164, 73, 163], [ 36, 28, 237], [0, 0, 0]]])

    # 二次元配列（グレースケール）
    gray = np.array([[138, 142, 98],
                     [0, 255, 195],
                     [120, 138, 0]])

    # 画像ファイルに出力
    cv2.imwrite("output1.jpg", img)
    cv2.imwrite("output2.jpg", img2)
    cv2.imwrite("output3.jpg", gray)


if __name__ == "__main__":
    main()
