# -*- coding: utf-8 -*-
import cv2
import numpy as np

def main()
    # キャプチャー
    capture = cv2.VideoCapture(0)
    
    # 最初のフレームを背景画像に設定
    ret, bg = capture.read()
    
    # カウント用変数
    i = 0
    
    while(cap.isOpened()):
        #フレームの取得
        ret,frame = capture.read()
        
        # グレースケール変換
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # 差分の絶対値を計算
        mask = cv2.absdiff(gray, bg)
        
        # 差分画像を二値化してマスク画像を算出
        mask[mask < 20] = 0
        mask[mask >= 20] = 255
        
        # マスク画像を表示
        cv2.imshow("Mask", mask)
        i += 1
        
        # 背景画像の更新（一定間隔）
        if(i > 20):
            ret,frame = capture.read()
            i = 0
            
        # qキーが押されたら途中終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
