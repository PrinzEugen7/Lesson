#-*- coding:utf-8 -*-
import cv2
import numpy as np

def DoM(gray, ksize1, ksize2):

    # カーネルサイズの異なる2つのメディアンフィルタ処理
    m1 = cv2.medianBlur(gray, ksize1)
    m2 = cv2.medianBlur(gray, ksize2)

    return m2 - m1


def main():
    # 入力画像を読み込み
    img = cv2.imread("input.jpg")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # DoMフィルタ処理
    dst = DoM(gray, 3, 5)

    # 結果を出力
    cv2.imwrite("output.jpg", dst )
    

if __name__ == "__main__":
    main()
