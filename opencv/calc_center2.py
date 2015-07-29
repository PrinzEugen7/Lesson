# -*- coding: utf-8 -*-
import cv2
import numpy as np

def main():
    # 画像取得・変換
    im = cv2.imread("test.png")                     # 入力画像の取得
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)     # 入力画像をグレースケール変換
    th = cv2.threshold(gray,127,255,0)[1]           # グレースケール画像の2値化
    # 輪郭抽出
    cnts = cv2.findContours(th,1,2)[0]              # グレースケール画像から輪郭検出
    areas = [cv2.contourArea(cnt) for cnt in cnts]
    cnt_max = [cnts[areas.index(max(areas))]][0]    # 最大の輪郭を抽出
    # 最大面積領域の重心を計算する
    M = cv2.moments(cnt_max)
    (cx, cy) = ( int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]) )
    cv2.circle(im,(cx,cy),5, (0,0,255), -1)         # 重心を赤円で描く
    # 結果表示
    cv2.imshow("Show Image",im)                     # 画像の表示
    cv2.waitKey(0)                                  # キー入力待機
    cv2.destroyAllWindows()                         # ウィンドウ破棄


if __name__ == "__main__":
    main()
