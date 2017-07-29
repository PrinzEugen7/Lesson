#-*- coding:utf-8 -*-
import cv2
import numpy as np

# 膨張処理
def dilate(src, ksize=3):
    h, w = src.shape
    dst = src.copy()
    d = int((ksize-1)/2)

    for y in range(0, h):
        for x in range(0, w):
            if np.count_nonzero(src[y-d:y+d+1, x-d:x+d+1]) > 0:
                dst[y][x] = 255

    return dst

# 収縮処理
def erode(src, ksize=3):

    h, w = src.shape
    dst = src.copy()
    d = int((ksize-1)/2)

    for y in range(0, h):
        for x in range(0, w):
            if np.count_nonzero(src[y-d:y+d+1, x-d:x+d+1]) < ksize**2:
                dst[y][x] = 0

    return dst

def main():
    # 入力画像を読み込み
    img = cv2.imread("input.jpg")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # 二値化処理
    gray[gray<127] = 0
    gray[gray>=127] = 255

    # 膨張・収縮処理(方法1)
    dilate1 = dilate(gray, ksize=3)
    erode1 = erode(dilate1, ksize=3)

    # 膨張・収縮処理(方法2)
    # 8近傍で処理
    kernel = np.array([[1, 1, 1],
                       [1, 1, 1],
                       [1, 1, 1]], np.uint8)

    dilate2 = cv2.dilate(gray, kernel)
    erode2 = cv2.erode(dilate2, kernel)

    # 結果を出力
    cv2.imwrite("dilate1.jpg", dilate1)
    cv2.imwrite("erode1.jpg", erode1)
    cv2.imwrite("dilate2.jpg", dilate2)
    cv2.imwrite("erode2.jpg", erode2)


if __name__ == "__main__":
    main()
