#-*- coding:utf-8 -*-
import cv2
import numpy as np

def template_matching_ssd(src, temp):
    # 画像の高さ・幅を取得
    h, w = src.shape
    ht, wt = temp.shape
   
    # スコア格納用の二次元配列
    score = np.empty((h-ht, w-wt))
  
    # 走査
    for dy in range(0, h - ht):
        for dx in range(0, w - wt):
            #　二乗誤差の和を計算
            diff = (src[dy:dy + ht, dx:dx + wt] - temp)**2
            score[dy, dx] = diff.sum()

    # スコアが最小の走査位置を返す
    pt = np.unravel_index(score.argmin(), score.shape)

    return (pt[1], pt[0])


def main():
    # 入力画像とテンプレート画像をで取得
    img = cv2.imread("input.png")
    temp = cv2.imread("temp.png")
    img2 = img.copy()
    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)   
    temp = cv2.cvtColor(temp, cv2.COLOR_RGB2GRAY)   

    # テンプレート画像の高さ・幅
    h, w = temp.shape

    # テンプレートマッチング（NumPyで実装）
    pt = template_matching_ssd(gray, temp)

    # テンプレートマッチング（OpenCVで実装）
    #match = cv2.matchTemplate(gray, temp, cv2.TM_SQDIFF)
    #min_value, max_value, min_pt, max_pt = cv2.minMaxLoc(match)
    #pt = min_pt

    # テンプレートマッチングの結果を出力
    cv2.rectangle(img, (pt[0], pt[1] ), (pt[0] + w, pt[1] + h), (0,0,200), 3)
    cv2.imwrite("output.png", img)


if __name__ == "__main__":
    main()
