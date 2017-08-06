#-*- coding:utf-8 -*-
import cv2
import numpy as np


def main():
    # 入力画像を読み込み
    img = cv2.imread("input.jpg")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # 線形濃度変換
    a, k = 0.7, 20
    zmin, zmax = 20.0, 220.0
    # gray = a * gray    # 変換1
    # gray = gray + k    # 変換2
    gray = a * (gray - 127.0) + 127.0 # 変換3
    #gray = gray.max() * (gray - zmin)/(zmax - zmin) # 変換4

    # 画素値を0～255の範囲内に収める
    gray[gray<0] = 0
    gray[gray>255] = 255

    # 結果の出力
    cv2.imwrite("output.jpg", gray)


if __name__ == "__main__":
    main()

