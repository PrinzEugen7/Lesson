#-*- coding:utf-8 -*-
import cv2
import numpy as np

# DoGフィルタ
def DoG(gray, ksize, sigma1, sigma2):
    # 標準偏差が異なる2つのガウシアン画像を算出
    g1 = cv2.GaussianBlur(gray, ksize, sigma1)
    g2 = cv2.GaussianBlur(gray, ksize, sigma2)
    # 2つのガウシアン画像の差分を出力
    return g1 - g2
 

def main():
    # 入力画像を読み込み
    img = cv2.imread("input.jpg")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # DoGフィルタ処理
    dst = DoG(gray, (3,3), 1.3, 2.6)

    # 結果を出力
    cv2.imwrite("output.jpg", dst )
    

if __name__ == "__main__":
    main()

