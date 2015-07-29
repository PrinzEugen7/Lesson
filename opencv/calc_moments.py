# -*- coding: utf-8 -*-
import cv2

def main():
    # 背景,
    im = cv2.imread("test.jpg",0)       #入力画像の取得
    area = cv2.countNonZero(im)         # 白色領域の面積を計算
    print (u"白色領域のピクセル数：" + str(area) )


if __name__ == "__main__":
    main()
