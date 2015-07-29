# -*- coding: utf-8 -*-
import cv2

def main():
    cap = cv2.VideoCapture(0)                                           # カメラのキャプチャー
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")  # 顔探索用の機械学習ファイルを取得
    while(1):
        ret, im = cap.read()                                            # カメラからフレームの取得
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)                     # 高速化1(グレースケール変換)
        gray = cv2.resize(gray,(gray.shape[1]/2,gray.shape[0]/2))       # 高速化2(フレームのサイズを半分)
        face = cascade.detectMultiScale(gray, 1.1, 3)                   # 顔探索(画像,縮小スケール,最低矩形数)
        # 顔検出した部分を長方形で囲う
        for (x, y, w, h) in face:
            gray2 = gray[y:y+h, x:x+w]
            gray2 = cv2.resize(gray2, (w/20, h/20))
            gray2 = cv2.resize(gray2, (w, h), interpolation=cv2.cv.CV_INTER_NN)
            gray[y:y+h, x:x+w] = gray2

        cv2.imshow("Camera",gray)   # 結果表示
        # キーが押されたらループから抜ける
        if cv2.waitKey(10) > 0:
            cap.release()           # キャプチャー解放
            cv2.destroyAllWindows() # ウィンドウ破棄
            break


if __name__ == '__main__':
    main()
