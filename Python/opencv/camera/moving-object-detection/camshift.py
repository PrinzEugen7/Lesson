# -*- coding: utf-8 -*-
import cv2
import numpy as np


def main():
    
    # カメラのキャプチャ
    cap = cv2.VideoCapture("input.mp4")
    x, y, w, h = 150,150,200,200       # 追跡領域(始点(320,240)から縦横200pxの矩形)
    hsv_min = np.array([20,128,0])
    hsv_max = np.array([200,255,255])
    frame = cap.read()[1]                                              # 最初のフレームを取得
    target = (x, y, w, h)
    hsv =  cv2.cvtColor(frame[y:y+h, x:x+w], cv2.COLOR_BGR2HSV)   # HSV色空間に変換
    mask = cv2.inRange(hsv, hsv_min, hsv_max)    # マスク画像の作成
    hist = cv2.calcHist([hsv],[0],mask,[180],[0,180])               # ヒストグラムの計算
    cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)                  # ヒストグラム正規化

    while(cap.isOpened()):
        frame = cap.read()[1]                                          # フレームの取得
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)                  # HSV色空間に変換
        bp = cv2.calcBackProject([hsv],[0],hist,[0,180],1)         # 現フレームと追跡領域のヒストグラムの類似度を計算
        # Camshift法で追跡対象(領域)の位置を計算
        x, y, w, h = cv2.CamShift(bp, target, (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1))[1]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,200),2)             # 追跡領域を矩形で描画
        cv2.imshow("Frame", frame)                                       # 結果の表示
        target = (x, y, w, h) # 追跡領域の更新

        # qキーが押されたら途中終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

