# -*- coding: utf-8 -*-
import cv2

def main():
    # 入力画像の取得
    im = cv2.imread("test.png")
    # モザイク加工する部分
    x, y, w, h = 100, 0, 150, 100       # モザイク加工する部分
    im2 = im[y:y+h, x:x+w]
    # 選択した部分にモザイク処理を施す
    im2 = cv2.resize(im2, (w/5, h/5))
    im2 = cv2.resize(im2, (w, h), interpolation=cv2.cv.CV_INTER_NN)
    im[y:y+h, x:x+w] = im2
    # 結果表示
    cv2.imshow("mosaic",im)
    cv2.waitKey(0)                      # キー入力待機
    cv2.destroyAllWindows()             # ウィンドウ破棄


if __name__ == "__main__":
    main()
