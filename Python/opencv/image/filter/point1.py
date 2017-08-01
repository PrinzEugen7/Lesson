#-*- coding:utf-8 -*-
import cv2
import numpy as np
    
def main():
    # 入力画像を読み込み
    img = cv2.imread("input.jpg")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # カーネル
    kernel = np.array([[0, 0, 0],
                       [-1, 0, 1],
                       [0, 0, 0]])

    # データ型がcv2.CV_8U(-1)
    dst1 = cv2.filter2D(gray,-1, kernel)

    # データ型がcv2.CV_64F
    dst2 = cv2.filter2D(gray,cv2.CV_64F, kernel)

    # 画像配列の中身出力
    print("dst1=\n", dst1)
    print("\n\n")
    print("dst2=\n", dst2)

    # 結果を出力
    cv2.imwrite("output1.jpg", dst1 )
    cv2.imwrite("output2.jpg", np.uint8(np.abs(dst2)) )
 
 
if __name__ == "__main__":
    main()
