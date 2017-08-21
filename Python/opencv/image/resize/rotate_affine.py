# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 最近傍補間法でリサイズ
def rotate_affine(src, rotate):

    # 元画像のサイズを取得
    h, w = src.shape[0], src.shape[1]

    # 出力画像用の配列生成（要素は全て空）
    dst = np.zeros((h,w))

    theta = np.radians(rotate)

    # 最近傍補間
    for y in range(0, h):
        for x in range(0, w):
            xi = int(round( x*np.cos(theta) + y*np.sin(theta) ))
            yi = int(round( -x*np.sin(theta) + y*np.cos(theta) ))
                
            #if xi > w - 1: xi = w - 1
            #if yi > h - 1: yi = h - 1 
            #print(xi, yi)
            if yi < h - 1 and xi < w -1:dst[y][x] = src[yi][xi]

    return dst


def main():

    # 入力画像の読み込み
    img = cv2.imread("input.jpg")
    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 方法1(NumPy）
    dst1 = rotate_affine(gray, rotate=-20)

    # 方法2(OpenCV)
    size = tuple([gray.shape[1], gray.shape[0]])# 画像サイズの取得(横, 縦)
    center = tuple([int(size[0]/2), int(size[1]/2)])    # 画像の中心位置(x, y)
    angle, scale = 20.0, 1.0    # 回転角度・拡大率
    R = cv2.getRotationMatrix2D(center, angle, scale)    # 回転変換行列の算出
    dst2 = cv2.warpAffine(img, R, size, flags=cv2.INTER_CUBIC)    # アフィン変換

    # 結果を出力
    cv2.imwrite("output1.jpg", dst1)
    cv2.imwrite("output2.jpg", dst2)


if __name__ == "__main__":
    main()
