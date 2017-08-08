# -*- coding: utf-8 -*-
import cv2
import numpy as np

x0,dx,y0,dy = 320,240,200,200       # 追跡領域(始点(320,240)から縦横200pxの矩形)
hsv_min = np.array((0,50,30))
hsv_max = np.array((170,255,255))

def main():
    cap = cv2.VideoCapture(0)                                       # カメラのキャプチャー
    im = cap.read()[1]                                              # 最初のフレームを取得
    target = (x0,y0,dx,dy)
    hsv =  cv2.cvtColor(im[y0:y0+dy,x0:x0+dx], cv2.COLOR_BGR2HSV)   # HSV色空間に変換
    mask = cv2.inRange(hsv, hsv_min, hsv_max)    # マスク画像の作成
    hist = cv2.calcHist([hsv],[0],mask,[180],[0,180])               # ヒストグラムの計算
    cv2.normalize(hist,hist,0,255,cv2.NORM_MINMAX)                  # ヒストグラム正規化

    while(1):
        im = cap.read()[1]                                          # フレームの取得
        hsv2 = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)                  # HSV色空間に変換
        bp = cv2.calcBackProject([hsv2],[0],hist,[0,180],1)         # 現フレームと追跡領域のヒストグラムの類似度を計算
        # MeanShift法で追跡対象(領域)の位置を計算
        x,y,w,h = cv2.meanShift(bp, target, (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1))[1]
        cv2.rectangle(im, (x,y), (x+w,y+h),(0,0,200),2)             # 追跡領域を矩形で描画
        cv2.imshow("Test",im)                                       # 結果の表示
        target = (x,y,w,h)                                          # 追跡領域の更新
        # 任意のキーが押されたら終了
        if cv2.waitKey(10) > 0:
            cap.release()               # キャプチャー解放
            cv2.destroyAllWindows()     # ウィンドウ破棄
            break

if __name__ == '__main__':
main()
