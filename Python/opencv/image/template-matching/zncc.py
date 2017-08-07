#-*- coding:utf-8 -*-
import cv2
import numpy as np

def template_matching_zncc(src, temp):
    # 画像の高さ・幅を取得
    h, w = src.shape
    ht, wt = temp.shape
    
    # スコア格納用の2次元リスト
    score = np.empty((h-ht, w-wt))
    ave_temp = temp/9   

    # 走査
    for dy in range(0, h - ht):
        for dx in range(0, w - wt):
            roi = src[dy:dy + ht, dx:dx + wt]
            ave_src = roi/9
            num = np.sum( (roi - ave_src) * (temp - ave_temp) )
            den = np.sqrt(np.sum(roi - ave_src) ** 2) / np.sqrt(np.sum(temp - ave_temp) ** 2)
            if den == 0: score[dy, dx] = 0
            score[dy, dx] = num / den

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
    pt = template_matching_zncc(gray, temp)

    # テンプレートマッチング（OpenCVで実装）
    #match = cv2.matchTemplate(gray, temp, cv2.TM_CCORR_NORMED)
    #min_value, max_value, min_pt, max_pt = cv2.minMaxLoc(match)
    #pt = max_pt

    # テンプレートマッチングの結果を出力
    cv2.rectangle(img, (pt[0], pt[1] ), (pt[0] + w, pt[1] + h), (0,0,200), 3)
    cv2.imwrite("output.png", img)


if __name__ == "__main__":
    main()
