# -*- coding: utf-8 -*-
import cv2
import numpy as np
from numpy import*

g_min = np.array([40,10,0])
g_max = np.array([70,255,255])
# 膨張化用のカーネル
k = np.ones((5,5),np.uint8)

##----------------------
## カラートラッキング
##----------------------
def color_track(im,h_min,h_max):

    im_h = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)# RGB色空間からHSV色空間に変換
    im_m = cv2.inRange(im_h,h_min,h_max)      # マスク画像の生成
    im_m = cv2.medianBlur(im_m,7)             # 平滑化
    im_m = cv2.dilate(im_m,k,iterations=1)    # 膨張化
    im_c = cv2.bitwise_and(im,im,mask=im_m)   # 色領域抽出

    return im_m,im_c

##----------------------
## Main
##----------------------
def main():
    # カメラ指定
    cap = cv2.VideoCapture(0)
    im = cap.read()[1]
    # 計算高速化のために画像サイズを1/2
    im = cv2.resize(im,(im.shape[1]/2,im.shape[0]/2))
    im_m,im_c = color_track(im,g_min,g_max)
    M0 = np.count_nonzero(im_m)
    D0=50
    while True:
        # 入力画像の取得
        im = cap.read()[1]
        # 計算高速化のために画像サイズを1/2
        im = cv2.resize(im,(im.shape[1]/2,im.shape[0]/2))
        im_m,im_c = color_track(im,g_min,g_max)
        # 白色領域の画素数を計算
        M = np.count_nonzero(im_m)
        D = format( (sqrt(M0)/sqrt(M))*D0,".2f")
        # マスク画像から指定した色の領域を抽出
        cv2.putText(im_m,"Moment:"+str(M),(30,30),1,1.5,(50),2)
        cv2.putText(im_m,"Distance:"+str(D),(30,70),1,1.5,(50),2)
        # 結果表示
        cv2.imshow("Camera",im)
        cv2.imshow("Mask",im_m)
        cv2.imshow("Color Tracking",im_c)
        # キーが押されたらループから抜ける
        if cv2.waitKey(10) > 0:
            cap.release()
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':

    main()
