#-*- coding:utf-8 -*-
import cv2
import numpy as np

def template_matching_sad(img, temp):
    # 画像の高さ・幅を取得
    h, w = img.shape
    ht, wt = temp.shape
    
    # スコア格納用の2次元リスト
    score = np.empty((h-ht,w-wt))
    
    # 走査
    for dy in range(0, h - ht):
        for dx in range(0, w - wt):
            # 差分の絶対和を計算
            diff = np.abs(img[dy:dy + ht, dx:dx + wt] - temp)
            score[dy, dx] = diff.sum()
            
    # スコアが最小の走査位置を返す
    return np.unravel_index(score.argmin(), score.shape)


def main():
    # 入力画像とテンプレート画像をグレースケールで取得
    img = cv2.imread("input.jpg", 0)
    temp = cv2.imread("temp.jpg", 0)
    
    # テンプレートマッチング（評価値SAD）
    point = template_matching_sad(img, temp)
    
    # 入力画像をRGBに変換
    img2 = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    
    # テンプレートマッチングの結果を出力
    cv2.rectangle(img2, (point[1], point[0] ), (point[1] + temp.shape[0], point[0] + temp.shape[1]), (0,0,200), 3)
    cv2.imwrite("result.jpg", img2)
    
if __name__ == "__main__":
    main()
