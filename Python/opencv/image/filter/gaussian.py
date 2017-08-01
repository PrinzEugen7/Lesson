#-*- coding:utf-8 -*-
import cv2
import numpy as np

def gaussian_filter(src, kernel):
    # カーネルサイズ
    m, n = kernel.shape
    
    # 畳み込み演算をしない領域の幅
    d = int((m-1)/2)
    h, w = src.shape[0], src.shape[1]
    
    # 出力画像用の配列（要素値は入力画像と同じ）
    dst = src.copy()

    for y in range(d, h - d):
        for x in range(d, w - d):
            # 畳み込み演算
            dst[y][x] = np.sum(src[y-d:y+d+1, x-d:x+d+1]*kernel)
            
    return dst
    
def main():
    # 入力画像を読み込み
    img = cv2.imread("input.jpg")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    # カーネル
    kernel = np.array([[1/16, 1/8, 1/16],
                       [1/8, 1/4, 1/8],
                       [1/16, 1/8, 1/16]])

    # 方法1
    dst1 = gaussian_filter(gray, kernel)
    
    # 方法2       
    dst2 = cv2.filter2D(gray, -1, kernel)
    
    # 方法3
    dst3 = cv2.GaussianBlur(gray, ksize=(3,3), sigmaX=1.3)
    
    # 結果を出力
    cv2.imwrite("output1.jpg", dst1)
    cv2.imwrite("output2.jpg", dst2)
    cv2.imwrite("output3.jpg", dst3)

    
if __name__ == "__main__":
    main()
