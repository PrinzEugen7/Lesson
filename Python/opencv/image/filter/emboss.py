#-*- coding:utf-8 -*-
import cv2
import numpy as np

def emboss_filter(src, kernel, offset=128):
    # カーネルサイズ
    m, n = kernel.shape
    
    # 畳み込み演算をしない領域の幅
    d = int((m-1)/2)
    h, w = src.shape[0], src.shape[1]

    # 出力画像用の配列（要素は全てoffset値）
    dst = np.empty((h,w))
    dst.fill(offset)
    
    for y in range(d, h - d):
        for x in range(d, w - d):
            # 畳み込み演算
            dst[y][x] = np.sum(src[y-d:y+d+1, x-d:x+d+1]*kernel) + offset
            
    return dst
    
def main():
    # 入力画像をグレースケールで読み込み
    gray = cv2.imread("input.jpg", 0)
    
    # カーネル（オペレータ）
    kernel = np.array([[-2, -1, 0],
                       [-1, 1, 1],
                       [-1, 1, 2]])

    # オフセット値
    offset = 128
    
    # 方法1
    dst1 = emboss_filter(gray, kernel, offset)
    
    # 方法2       
    dst2 = cv2.filter2D(gray, -1, kernel, delta=offset)
    
    # 結果を出力
    cv2.imwrite("output1.jpg", dst1)
    cv2.imwrite("output2.jpg", dst2)

    
if __name__ == "__main__":
    main()
