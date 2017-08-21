# -*- coding: utf-8 -*-
import cv2
import numpy as np


def main():

    # 入力画像の読み込み
    img = cv2.imread("input.jpg")

    # 画像のサイズ取得
    size = tuple([img.shape[1], img.shape[0]])

    # 回転の中心座標（画像の中心）
    center = tuple([int(size[0]/2), int(size[1]/2)])

    # 回転角度・拡大率
    angle, scale = 20.0, 1.0    

    # 回転行列の計算
    R = cv2.getRotationMatrix2D(center, angle, scale) 

    # アフィン変換
    dst = cv2.warpAffine(img, R, size, flags=cv2.INTER_CUBIC) 

    # 結果を出力
    cv2.imwrite("output.jpg", dst)


if __name__ == "__main__":
    main()
