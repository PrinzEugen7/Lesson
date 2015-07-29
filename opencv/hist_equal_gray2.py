# -*- coding: utf-8 -*-
import cv
# import cv2.cv as cv

if __name__ == '__main__':

    # 画像取得
    im = cv.LoadImage("test.jpg")
    # 画像データ用意
    gray = cv.CreateImage(cv.GetSize(im), 8, 1)
    eq = cv.CreateImage(cv.GetSize(gray), 8, 1)
    # ヒストグラム平坦化
    cv.CvtColor(im, gray,cv.CV_BGR2GRAY)
    cv.EqualizeHist(gray, eq)
    # ウィンドウ作成
    cv.NamedWindow("Show Image")
    # 画像表示
    cv.ShowImage("Show Image",eq)
    # キー入力待機
    cv.WaitKey(0)
    # ウィンドウ破棄
    cv.DestroyAllWindows()
    # 画像保存
    cv.SaveImage("eq.jpg",eq)
