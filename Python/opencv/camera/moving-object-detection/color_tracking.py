# -*- coding: utf-8 -*-
import cv2
import numpy as np


def main():
    # 赤色のHSVの値域を指定
    hsv_min = np.array([20,128,0])
    hsv_max = np.array([200,255,255])
    
    # カメラのキャプチャ
    cap = cv2.VideoCapture(0)
    
    while(cap.isOpened()):
        # フレームを取得
        ret, frame = cap.read()
        
        # HSV色空間に変換
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 赤色領域のみを取り出してマスク画像を出力
        mask = cv2.inRange(hsv, hsv_min, hsv_max)
        
        # 結果表示
        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", mask)

        # qキーが押されたら途中終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
