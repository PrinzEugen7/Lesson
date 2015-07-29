# -*- coding: utf-8 -*-
import cv2
import numpy as np

def main():
    roi = (0,0,500,350)                     # 処理する領域を指定
    im = cv2.imread("test.png")             # 画像の取得
    mask = np.zeros(im.shape[:2],np.uint8)  # マスク用の画像オブジェクト生成
    bg = np.zeros((1,65),np.float64)        # 背景用の画像オブジェクト生成
    fg = np.zeros((1,65),np.float64)        # 前景用の画像オブジェクト生成
    # グラフカットで背景と前景に領域を分割
    cv2.grabCut(im, mask, roi, bg, fg, 5, cv2.GC_INIT_WITH_RECT)
    mask = np.where((mask==2)|(mask==0),0,1).astype("uint8")
    im = im*mask[:,:,np.newaxis]           # 画像と前景マスクから前景領域のみを抽出
    cv2.imshow("Test",im)
    cv2.waitKey(0)                          # キー入力待機
    cv2.destroyAllWindows()                 # ウィンドウ破棄


if __name__ == "__main__":
    main()
