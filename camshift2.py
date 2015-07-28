# -*- coding: utf-8 -*-
import cv2
import numpy as np

# クリックされた座標
(cx, cy) = (0, 0)
click_r = 0

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

def main():
    cap = cv2.VideoCapture(0)    # カメラのキャプチャー
    ret,im = cap.read()          # 最初のフレームを取得
    r,h,c,w = 200,50,400,50      # 追跡したい領域の初期設定
    h0 = 0
    roi = im[r:r+h, c:c+w]       # 追跡のためのROIを設定
    hsv_roi =  cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)                             # HSV色空間に変換
    mask = cv2.inRange(hsv_roi, np.array((0, 60,32)), np.array((180,255,255)))  # マスク画像の作成
    roi_hist = cv2.calcHist([hsv_roi],[0],mask,[180],[0,180])                   # ヒストグラムの計算
    cv2.normalize(roi_hist,roi_hist,0,255,cv2.NORM_MINMAX)                      # ヒストグラムの正規化
    term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1 )      # 終了基準の設定
    while(1):
        ret ,im = cap.read()
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)               # HSV色空間に変換
        dst = cv2.calcBackProject([hsv],[0],roi_hist,[0,180],1) # バックプロジェクションの計算
        cv2.setMouseCallback("CamShift",onMouse)                # マウスイベント
        # 左クリックされた場合
        if(cx!=0):
            (c,r,w,h) = (cx-25, cy-25, 50, 50)
        track_window = (c,r,w,h)
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)  # 新しい場所を取得するためにcamshiftを適用
        (x,y,w,h) = track_window
        frame = cv2.rectangle(im, (x,y), (x+w,y+h),(0,0,200),2)     # 追跡している領域の表示
        cv2.circle(im,(cx,cy),10,(220,0,0), -1)                     # 左クリックした場所を円で表示
        cv2.imshow("CamShift",im)                                   # 映像の表示

        # 任意のキーが押されたら終了
        if cv2.waitKey(10) > 0:
            cap.release()
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    main()
