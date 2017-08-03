#-*- coding:utf-8 -*-
import cv2
import numpy as np

def XDoG(gray, ksize, sigma1, sigma2, p, epsilon, phi):

    g1 = cv2.GaussianBlur(gray, ksize, sigma1)
    g2 = cv2.GaussianBlur(gray, ksize, sigma2)
    s = (1+p) * g1 - p * g2
    si = np.multiply(gray, s)
    T = np.zeros(si.shape)
    si_bright = si >= epsilon
    si_dark = si < epsilon
    T[si_bright] = 1.0
    T[si_dark] = 1.0 + np.tanh( phi * (si[si_dark] - epsilon))
    return T


def main():
    # 入力画像を読み込み
    img = cv2.imread("input.jpg")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # DoGフィルタ処理
    dst = XDoG(gray, (3,3), 1.3, 2.6, 2, 1, 1.1)

    # 結果を出力
    cv2.imwrite("output.jpg", dst )
    

if __name__ == "__main__":
    main()

