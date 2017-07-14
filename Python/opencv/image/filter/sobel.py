#-*- coding:utf-8 -*-
import cv2
import numpy as np

def filter2d(src, kernel):
    m, n = kernel.shape
    h = src.shape[0] - m + 1
    w = src.shape[1] - m + 1
    dst = np.zeros((h,w))
    for y in range(h):
        for x in range(w):
            dst[y][x] = np.sum(src[y:y+m, x:x+m]*kernel)
    return dst
    
def main():
    # 入力画像をグレースケールで読み込み
    gray = cv2.imread("input.jpg", 0)
    
    # カーネル（オペレータ）
    kernel = np.array([[-1, 0, 1],
                       [-2, 0, 2],
                       [-1, 0, 1]])

    # 方法1
    dst1 = filter2d(gray, kernel)
    
    # 方法2       
    dst2 = cv2.filter2D(gray, -1, kernel)
    
    # 方法3
    dst3 = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
    
    # 結果を出力
    cv2.imwrite("output1.jpg", dst1)
    cv2.imwrite("output2.jpg", dst2)
    cv2.imwrite("output3.jpg", dst3)

    
if __name__ == "__main__":
    main()
