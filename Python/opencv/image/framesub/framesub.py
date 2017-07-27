#-*- coding:utf-8 -*-
import cv2
import numpy as np

def main():
    # 閾値
    T = 100
    
    # 3枚の画像を読み込む
    frame1 = cv2.imread("frame1.png", 0)
    frame2 = cv2.imread("frame2.png", 0)
    frame3 = cv2.imread("frame3.png", 0)

    # 2枚の差分画像を求める
    diff1 = cv2.absdiff(frame1, frame2)
    diff2 = cv2.absdiff(frame2, frame3)
    
    # 差分画像の論理積を求める
    diff = cv2.bitwise_and(diff1, diff2)

    diff[np.where(diff > T)] = 255
    cv2.imwrite("diff.png", diff)

if __name__ == "__main__":
    main()
