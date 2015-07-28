 # -*- coding: utf-8 -*-
import numpy as np
import cv2

def main():
    n = 50
    cap = cv2.VideoCapture(0)                           # カメラのキャプチャ

    while(1):
        ret, im = cap.read()                            # カメラからフレームの取得
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)     # 画像のグレースケール変換
        edge = cv2.Canny(gray, 50, 150)                 # 輪郭線を検出
        edge = cv2.cvtColor(edge,cv2.COLOR_GRAY2BGR)	  # 輪郭画像をRGBに変換
        im = (im/n)*n                                   # 減色処理
        im = im - edge                                  # 輪郭線を除去
        cv2.imshow("Anime",im)
        k = cv2.waitKey(10)

        # Escキーが押されたら終了
        if k == 27:
            cap.release()
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()
