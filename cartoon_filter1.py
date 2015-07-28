# -*- coding: utf-8 -*-
import numpy as np
import cv2

# 減色処理
def subtractive_color(src, k):
    z = src.reshape((-1,3))         # 配列の次元数を2に変換
    z = np.float32(z)               # float型(32bit)に変換
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)            # kmeans関数の条件
    ret,label,center=cv2.kmeans(z, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)    # k-meansクラスタリングで減色処理
    center = np.uint8(center)       # データの型をuint8(画像データと同じ)に変換
    res = center[label.flatten()]   # labelを1次元配列に変換し、uint8型のデータに変換
    return res.reshape((src.shape)) # resを元画像と同じ次元数に変換


def main():
    im = cv2.imread("test.jpg")                     # 画像の取得
    im = subtractive_color(im, 8)                   # 減色処理
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)     # 画像のグレースケール変換
    edge = cv2.Canny(gray, 50, 150)                 # 輪郭線を検出
    edge = cv2.cvtColor(edge,cv2.COLOR_GRAY2BGR)	# 輪郭画像をRGBに変換
    im = im - edge                                  # 輪郭線を除去
    cv2.imshow("Result",im)                         # 結果を表示
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
