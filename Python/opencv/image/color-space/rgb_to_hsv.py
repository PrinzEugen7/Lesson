#-*- coding:utf-8 -*-
import cv2
import numpy as np


def rgb_to_hsv(src, ksize=3):
    # 高さ・幅・チャンネル数を取得
    h, w, c = src.shape
    
    # 入力画像と同じサイズで出力画像用の配列を生成(中身は空)
    dst = np.empty((h, w, c))

    for y in range(0, h):
        for x in range(0, w):
            # R, G, Bの値を取得して0～1の範囲内にする
            [b, g, r] = src[y][x]/255.0

            # R, G, Bの値から最大値と最小値を計算
            mx, mn = max(r, g, b), min(r, g, b)
            
            # 最大値 - 最小値
            diff = mx - mn

            # Hの値を計算
            if mx == mn : h = 0
            elif mx == r : h = 60 * ((g-b)/diff)     
            elif mx == g : h = 60 * ((b-r)/diff) + 120  
            elif mx == b : h = 60 * ((r-g)/diff) + 240
            if h < 0 : h = h + 360
                
            # Sの値を計算
            if mx != 0:s = diff/mx       
            else: s = 0
            
            # Vの値を計算
            v = mx
            
            # H, S, Vの値を0～255の範囲内にして格納
            dst[y][x] = [h, s * 255, v * 255]

    return dst


def main():
    # 入力画像の読み込み
    img = cv2.imread("input.jpg")

    # 方法1(NumPyで実装)
    hsv1 = rgb_to_hsv(img)
    
    # 方法2(OpenCVで実装)       
    hsv2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # 結果を出力
    cv2.imwrite("hsv1.jpg", hsv1)
    cv2.imwrite("hsv2.jpg", hsv2)


if __name__ == "__main__":
    main()
