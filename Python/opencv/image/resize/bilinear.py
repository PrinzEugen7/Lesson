# -*- coding: utf-8 -*-
import cv2
import numpy as np

# バイリニア補間法でリサイズ
def resize_bilinear(src, h, w):

    # 出力画像用の配列生成（要素は全て空）
    dst = np.empty((h,w))

    # 元画像のサイズを取得
    hi, wi = src.shape[0], src.shape[1]

    # 拡大率を計算
    ax = w / float(wi)
    ay = h / float(hi)
    
    # バイリニア補間法
    for y in range(0, h):
        for x in range(0, w):
            xi, yi = x/ax, y/ay
            x0, y0 = int(xi), int(yi)

             # 存在しない座標の処理
            if x0 > wi - 2: x0 = wi - 2
            if y0 > hi - 2: y0 = hi - 2
            
            # 重みの計算
            dx = xi - x0
            dy = yi - y0
            
            dst[y][x] = (1 - dx) * (1-dy) * src[y0][x0] + dx * (1-dy) * src[y0][x0+1] + (1-dx) * dy * src[y0][x0+1] + dx * dy * src[y0+1][x0+1]
            
    return dst


def main():

    # 入力画像の読み込み
    img = cv2.imread("input.jpg")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 方法1(NumPy）
    dst1 = resize_bilinear(gray, gray.shape[1]*2, gray.shape[0]*2)

    # 方法2(OpenCV)
    dst2 = cv2.resize(gray, (gray.shape[1]*2, gray.shape[0]*2), interpolation=cv2.INTER_LINEAR)

    # 結果を出力
    cv2.imwrite("output1.jpg", dst1)
    cv2.imwrite("output2.jpg", dst2)


if __name__ == "__main__":
    main()
