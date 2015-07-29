# -*- coding: utf-8 -*-
import cv2
import numpy as np

def main():

    cap = cv2.VideoCapture(0)        # カメラのキャプチャ

    while(1):
        ret, im = cap.read()
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
        cv2.imshow("CV2 Camera",im)
        # 緑色(HSV)の範囲を定義
        hsv_min = np.array([40,10,0])
        hsv_max = np.array([70,255,255])
        # マスク画像を用いて元画像から指定した色を抽出
        mask = cv2.inRange(hsv, hsv_min, hsv_max)
        im2 = cv2.bitwise_and(im,im, mask=mask)
        cv2.imshow("test",im2)
        # キーが押されたらループから抜ける
        if cv2.waitKey(10) > 0:
            cap.release()               # キャプチャー解放
            cv2.destroyAllWindows()     # ウィンドウ破棄
            break


if __name__ == '__main__':
    main()
