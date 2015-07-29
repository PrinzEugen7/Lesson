# -*- coding: utf-8 -*-
import cv2

def main():
    # 画像取得
    im = cv2.imread("test.png")                 # 入力画像の取得
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) # 入力画像をグレースケール変換
    th = cv2.threshold(gray,127,255,0)[1]       # グレースケール画像の2値化
    # 輪郭抽出
    cnts = cv2.findContours(th,1,2)[0]          # グレースケール画像から輪郭検出
    cv2.drawContours(im,cnts,-2,(255,0,0),-1)   # 最大の輪郭を描く
    # 結果表示
    cv2.imshow("Show Image",im)                 # 画像の表示
    cv2.waitKey(0)                              # キー入力待機
    cv2.destroyAllWindows()                     # ウィンドウ破棄


if __name__ == "__main__":
    main()
