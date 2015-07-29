# -*- coding: utf-8 -*-
import cv2

def main():
    # 入力画像とマスク画像の取得
    im = cv2.imread("test.png",1)
    mask = cv2.imread("mask.png",0)
    # マスク処理
    im2 = cv2.bitwise_and(im,im, mask=mask)
    # 結果表示
    cv2.imshow("Mask",im2)
    cv2.waitKey(0)                      # キー入力待機
    cv2.destroyAllWindows()             # ウィンドウ破棄


if __name__ == "__main__":
    main()
