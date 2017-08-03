#-*- coding:utf-8 -*-
import cv2
import numpy as np


def main():
    # 入力画像を読み込み
    img = cv2.imread("input.jpg")
    
    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # 画素値を表示
    print("gray=\n", gray)

    # 積分画像の作成
    integral = cv2.integral(gray)

    # 画素値を表示
    print("integral=\n", integral)


if __name__ == "__main__":
    main()
