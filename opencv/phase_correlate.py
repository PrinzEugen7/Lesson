# -*- coding: utf-8 -*-
import cv2
import numpy as np

def main():
    # 2枚の画像をグレースケールで取得
    im1 = cv2.imread("test1.png",0)
    im2 = cv2.imread("test2.png",0)
    # 画像データをfloat32型に型変換
    im1 = np.float32(im1)
    im2 = np.float32(im2)
    # 位相相関を計算して2枚の画像のズレを求める
    dx, dy = cv2.phaseCorrelate(im1,im2)
    print(u"x方向のズレ:"+str(dx))
    print(u"y方向のズレ:"+str(dy))

if __name__ == '__main__':
    main()
