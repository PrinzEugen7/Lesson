#-*- coding:utf-8 -*-
import cv2
import numpy as np


def main():
    # 画像の読み込み(RGB)
    img = cv2.imread("input.png")

    # 画像の読み込み(グレースケール)
    gray = cv2.imread("input.png", 0)

    # 画像の読み込み(RGBA)
    rgba = cv2.imread("input.png", -1)

    # 画素値の表示
    print("rgb=", img)
    print("\n------------------------\n")
    print("gray=", gray)
    print("\n------------------------\n")
    print("rgba=", rgba)


if __name__ == "__main__":
    main()
