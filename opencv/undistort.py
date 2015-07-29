# -*- coding: utf-8 -*-
import cv2
import numpy as np

def main():
    # カメラの内部パラメータ
    K = np.array([[813.03410511, 0, 322.04748609],
                  [0, 815.50965611, 234.09421823],
                  [0, 0, 1]])
    d = np.array([0.05957042, -0.83315378, -0.00415272, -0.0033495, 3.08794282])

    # 補正する画像の取得
    im = cv2.imread("test.jpg")
    # 画像の高さ，幅の取得
    h, w = im.shape[:2]

    # 歪み補正
    newcamera, roi = cv2.getOptimalNewCameraMatrix(K, d, (w,h), 0)
    im2 = cv2.undistort(im, K, d, None, newcamera)
    # 補正した画像の保存
    cv2.imwrite("test2.jpg",im2)

if __name__ == '__main__':
    main()
