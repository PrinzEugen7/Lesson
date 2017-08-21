# -*- coding: utf-8 -*-
import cv2


def main():

    # 入力画像の読み込み
    img = cv2.imread("input.jpg")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # HoG特徴量 + SVMで人の識別器を作成
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    hogParams = {'winStride': (8, 8), 'padding': (32, 32), 'scale': 1.05}

    # 作成した識別器で人を検出
    human, r = hog.detectMultiScale(gray, **hogParams)

    # 人の領域を赤色の矩形で囲む
    for (x, y, w, h) in human:
        cv2.rectangle(img, (x, y), (x + w, y+h), (0,0,200), 3)

    # 結果を出力
    cv2.imwrite("result.jpg",img)


if __name__ == '__main__':
    main()
