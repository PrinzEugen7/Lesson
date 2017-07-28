#-*- coding:utf-8 -*-
import cv2
import numpy as np

def filter2d(src, kernel):
    # カーネルサイズ
    m, n = kernel.shape
    
    # 畳み込み演算をしない領域の幅
    d = int((m-1)/2)
    h, w = src.shape[0], src.shape[1]
    
    # 出力画像用の配列（要素は全て0）
    dst = np.zeros((h,w))
    
    for y in range(d, h - d):
        for x in range(d, w - d):
            # 畳み込み演算
            dst[y][x] = np.sum(src[y-d:y+d+1, x-d:x+d+1]*kernel)
            
    return dst
    
def main():
    # 入力画像をグレースケールで読み込み
    gray = cv2.imread("input.jpg", 0)
    
    # カーネル（縦方向の輪郭検出用）
    kernel = np.array([[1, 1,  1],
                       [1, -8, 1],
                       [1, 1,  1]])

    # 方法1
    dst1 = filter2d(gray, kernel)
    
    # 方法2       
    dst2 = cv2.filter2D(gray, -1, kernel)
    
    # 方法3
    dst3 = cv2.Laplacian(gray, cv2.CV_32F, ksize=3)
    
    # 結果を出力
    cv2.imwrite("output1.jpg", dst1)
    cv2.imwrite("output2.jpg", dst2)
    cv2.imwrite("output3.jpg", dst3)

    
if __name__ == "__main__":
    main()
