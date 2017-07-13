#-*- coding:utf-8 -*-
import cv2

def rgb_to_gray(src):
     # チャンネル分解
     r, g, b = src[:,:,0], src[:,:,1], src[:,:,2]
     # R, G, Bの値からGrayの値に変換
     gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
     
     return gray   
    
def main():
    # 入力画像の読み込み
    img = cv2.imread("input.jpg")

    # 方法1
    gray1 = rgb_to_gray(img)
    
    # 方法2       
    gray2 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    # 結果を出力
    cv2.imwrite("gray1.jpg", gray1)
    cv2.imwrite("gray2.jpg", gray2)
    
if __name__ == "__main__":
    main()
