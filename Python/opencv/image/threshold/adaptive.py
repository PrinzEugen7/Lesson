#-*- coding:utf-8 -*-
import cv2
import numpy as np

def threshold(src, ksize=3, c=2):
    
    # 畳み込み演算をしない領域の幅
    d = int((ksize-1)/2)
    h, w = src.shape[0], src.shape[1]
    
    # 出力画像用の配列（要素は全て255）
    dst = np.empty((h,w))
    dst.fill(255)
    
    n = ksize**2

    for y in range(0, h):
        for x in range(0, w):
            # 近傍の画素値の平均から閾値を求める
            t = np.sum(src[y-d:y+d+1, x-d:x+d+1]) / n
            # 求めた閾値で二値化処理
            if(src[y][x] < t - c): dst[y][x] = 0
            else: dst[y][x] = 255

    return dst
    
def main():
    # 入力画像を読み込み
    img = cv2.imread("input.jpg")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # 方法1
    dst1 = threshold(gray, ksize=11, c=2)
    
    # 方法2       
    dst2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)

    
    # 結果を出力
    cv2.imwrite("output1.jpg", dst1)
    cv2.imwrite("output2.jpg", dst2)

    
if __name__ == "__main__":
    main()
