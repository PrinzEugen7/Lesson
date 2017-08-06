#-*- coding:utf-8 -*-
import cv2
import numpy as np


def main():
    # 画像の読み込み(グレースケール)
    gray = cv2.imread("input.png", 0)

    # 幅・高さ・チャンネル数の取得
    h, w = gray.shape

    # 画素数 = 幅 * 高さ
    s = w * h

    print("幅：", w)
    print("高さ：", h)
    print("画素数:", s)   
    print("データ型：", gray.dtype)


if __name__ == "__main__":
    main()
