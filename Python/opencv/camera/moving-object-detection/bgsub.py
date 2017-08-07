# -*- coding: utf-8 -*-
import cv2
import numpy as np

def main():

    i = 0      # カウント変数
    th = 30    # 差分画像の閾値
    
    # キャプチャー
    cap = cv2.VideoCapture(0)
    
    # 最初のフレームを背景画像に設定
    ret, bg = cap.read()

    # グレースケール変換
    bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY) 

    while(cap.isOpened()):
        # フレームの取得
        ret,frame = cap.read()
        
        # グレースケール変換
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # 差分の絶対値を計算
        mask = cv2.absdiff(gray, bg)
        
        # 差分画像を二値化してマスク画像を算出
        mask[mask < th] = 0
        mask[mask >= th] = 255
        
        # マスク画像を表示
        cv2.imshow("Mask", mask)
        i += 1
        
        # 背景画像の更新（一定間隔）
        if(i > 30):
            ret, bg = cap.read()
            bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY) 
            i = 0
            
        # qキーが押されたら途中終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
