# -*- coding: utf-8 -*-
import cv2


def main():
    im = cv2.imread("test.png")         # 入力画像の取得
    h,w = im.shape[0],im.shape[1]       # 画像の高さ,幅
    # 画像を1/10に縮小化した後、元サイズに戻す
    im2 = cv2.resize(im, (w/10, h/10))  # 画像
    mosaic = cv2.resize(im2, (w, h), interpolation=cv2.cv.CV_INTER_NN)
    # 結果表示
    cv2.imshow("mosaic",mosaic)
    cv2.waitKey(0)                      # キー入力待機
    cv2.destroyAllWindows()             # ウィンドウ破棄


if __name__ == "__main__":
    main()
