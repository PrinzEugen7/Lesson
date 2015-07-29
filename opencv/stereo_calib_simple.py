# -*- coding: utf-8 -*-
import cv2
import numpy as np
from numpy import*

# 緑色の領域(HSV)
g_min,g_max = np.array([30,70,30]),np.array([70,255,255])

#=== カラートラッキング(緑色)
def color_track(im,h_min,h_max):
    im_h = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)  # RGB色空間からHSV色空間に変換
    mask = cv2.inRange(im_h,h_min,h_max,)       # マスク画像の生成
    return mask

#=== 要素数が最大のインデックス
def index_emax(cnt,nmax=0,imax=-1):
    for i in range(len(cnt)):
        n_cnt = len(cnt[i])
        if n_cnt > nmax:
            nmax = n_cnt
            imax = i

    return imax

#=== 要素数が最大のインデックス
def mask_CoG(im,mask):
    # 紅色領域の輪郭を抽出
    cnt = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]
    n = index_emax(cnt)

    if n != -1:
        hull = cv2.convexHull(cnt[n])
        mask[:] = 0
        cv2.drawContours(mask,[hull],0,(255),-1)
        cv2.drawContours(im,[hull],0,(0,200,0),3)
        M = cv2.moments(cnt[n])
        if M["m00"] != 0:
            cx,cy = int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"])
        else:
            cx,cy = 320,240
    return im,mask,cx,cy


#=== Main
def main():
    # カメラの焦点距離，間隔
    z,d = 1000,214
    cap1 = cv2.VideoCapture(0)
    cap2 = cv2.VideoCapture(1)

    while True:
        # 左カメラ
        im1 = cap1.read()[1]
        mask1 = color_track(im1,g_min,g_max)
        im1,mask1,cx1,cy1 = mask_CoG(im1,mask1)
        # 右カメラ
        im2 = cap2.read()[1]
        mask2 = color_track(im2,g_min,g_max)
        im2,mask2,cx2,cy2 = mask_CoG(im2,mask2)
        # 視差
        dcx,dcy = abs(cx2-cx1),abs(cy2-cy1)
        # 焦点距離
        f = float(dcx)*z/d
        # 結果表示
        cv2.putText(im2,"(cx,cy): "+"("+str(dcx)+","+str(dcy)+")",(30,20),1,1.5,(70,70,220),2)
        cv2.putText(im2,"f: "+str(f),(30,70),1,1.5,(70,70,220),2)
        cv2.circle(im1,(cx1,cy1),5, (0,0,255), -1)
        cv2.circle(im2,(cx2,cy2),5, (0,0,255), -1)
        cv2.imshow("Left",im1)
        cv2.imshow("Right",im2)
        # キーが押されたらループから抜ける
        if cv2.waitKey(10) > 0:
            cap1.release()
            cap2.release()
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()
