# -*- coding: utf-8 -*-
import cv2
import numpy as np

(cx, cy) = (0, 0)           # クリックされた座標

# マウスクリックの処理
def onMouse(event, x, y, flags, param):
    global cx,cy,click_r
    if event == cv2.EVENT_MOUSEMOVE:return

    if event == cv2.EVENT_LBUTTONDOWN:
        (cx, cy) = (x, y)
        return

    if event == cv2.EVENT_RBUTTONDOWN:
        click_r = 1
        return

    click_r = 0

# カラートラッキング
def color_track(im,x,y):
    k = np.ones((5,5),np.uint8) # 膨張化用のカーネル
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)# RGB色空間からHSV色空間に変換
    h,s,v = hsv[y,x]        # HSVを抽出
    hsv_min = np.array([h-20,s-70,v-90])
    hsv_max = np.array([h+20,s+70,v+90])
    mask2 = cv2.inRange(hsv,hsv_min,hsv_max)      # マスク画像の生成
    mask2 = cv2.dilate(mask2,k,iterations=2)    # 膨張化
    mask2 = cv2.erode(mask2,k,iterations=2)    # 膨張化
    return mask2

# 要素数が最大のインデックス
def index_emax(cnt,nmax=0,imax=-1):
    for i in range(len(cnt)):
        ncnt = len(cnt[i])
        if ncnt > nmax:
            nmax = ncnt
            imax = i

    return imax

def main():
    (x,y)  = (0,0)
    while(1):
        im = cv2.imread("test.png")             # 画像取得
        cv2.setMouseCallback("Viewer",onMouse)                # マウスイベント
        # 左クリックされた場合
        if(cx!=0):
            (x,y) = (cx, cy)
        mask = color_track(im,x,y)
        cnt = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]
        n = index_emax(cnt)
        if n != -1:
            hull = cv2.convexHull(cnt[n])
            cv2.drawContours(im,[hull],0,(20,30,220),3)
        # 結果表示
        cv2.rectangle(im,(x-5,y-5),(x+5,y+5),(0, 50, 255), 2)
        cv2.imshow("Viewer",im)
        # 任意のキーが押されたら終了
        if cv2.waitKey(10) > 0:
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    main()
