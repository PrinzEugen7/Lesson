#-*- coding:utf-8 -*-
import cv2
import numpy as np


def main():
    # 画像の読み込み(RGB)
    img = cv2.imread("input.png")

    h, w, ch = img.shape

    # 画素数 = 幅 * 高さ
    s = w * h

    print("幅：", w)
    print("高さ：", h)
    print("チャンネル数:", ch)
    print("画素数:", s)   
    print("データ型：", img.dtype)


if __name__ == "__main__":
    main()
