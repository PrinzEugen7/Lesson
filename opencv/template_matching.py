# -*- coding:utf-8 -*-
import cv2


def main():
    # 画像の取得
    im = cv2.imread("fubuki.png")                               # 入力画像の取得
    temp = cv2.imread("template.png",0)                         # テンプレート画像をグレースケールで取得
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)                 # 入力画像のグレースケール変換
    w, h = temp.shape[::-1]                                     # テンプレート画像のサイズ
    # テンプレートマッチング
    res = cv2.matchTemplate(gray,temp,eval("cv2.TM_CCOEFF"))    # テンプレートマッチング処理
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)     # 一致した部分の位置情報を取得
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(im,top_left, bottom_right, (0,0,255), 2)      # 一致した部分を矩形で囲む
    # 結果の表示
    cv2.imshow("Template Matching",im)
    cv2.waitKey(0)                                              # キー入力待機
    cv2.destroyAllWindows()


if(__name__=="__main__"):
    main()
