# -*- coding: utf-8 -*-
import cv2
import numpy as np

# 減色処理
def sub_color(src, K):

    # 次元数を1落とす
    Z = src.reshape((-1,3))

    # float32型に変換
    Z = np.float32(Z)

    # 基準の定義
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

    # K-means法で減色
    ret, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # UINT8に変換
    center = np.uint8(center)

    res = center[label.flatten()]

    # 配列の次元数と入力画像と同じに戻す
    return res.reshape((src.shape))


def main():

    # 入力画像とスクリーントーン画像を取得
    img = cv2.imread("input.jpg") 

    # 減色処理(三値化)
    dst = sub_color(img, K=3)
    
    # 結果を出力
    cv2.imwrite("output.jpg", dst)


if __name__ == '__main__':
    main()
