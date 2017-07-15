#-*- coding:utf-8 -*-
import cv2
import numpy as np

def median_filter(src, kernel):
    # カーネルサイズ
    m, n = kernel.shape
    
    # 畳み込み演算をしない領域の幅
    d = int((m-1)/2)
    h, w = src.shape[0], src.shape[1]
    
    # 出力画像用の配列（要素は全て0）
    dst = np.zeros((h,w))
    
    for y in range(d, h - d - 1):
        for x in range(d, w - d - 1):
            # 畳み込み演算
            dst[y][x] = np.sum(src[y:y+m, x:x+m]*kernel)
            
    return dst
    
def main():
    # 入力画像をグレースケールで読み込み
    gray = cv2.imread("input.jpg", 0)

    # 方法1
    dst1 = median_filter(gray, kernel)
    
    # 方法2       
    dst2 = cv2.medianBlur(gray, ksize=3)
    
    # 方法3

    
    # 結果を出力
    cv2.imwrite("output1.jpg", dst1)
    cv2.imwrite("output2.jpg", dst2)

    
if __name__ == "__main__":
    main()
