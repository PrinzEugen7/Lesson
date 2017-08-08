# -*- coding: utf-8 -*-
import cv2
import numpy as np


def main():
    
    # カメラのキャプチャ
    cap = cv2.VideoCapture("input.mp4")

    while(cap.isOpened()):

        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 緑色(HSV)の範囲を定義
        hsv_min = np.array([20,128,0])
        hsv_max = np.array([200,255,255])

        # マスク画像を用いて元画像から指定した色を抽出
        mask = cv2.inRange(hsv, hsv_min, hsv_max)

        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", mask)

        # qキーが押されたら途中終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
