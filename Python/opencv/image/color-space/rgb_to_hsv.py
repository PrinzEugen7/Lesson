#-*- coding:utf-8 -*-
import cv2
import numpy as np

def rgb_to_hsv(src):
    src = src.astype('float')
    hsv = np.zeros_like(src)
    hsv[..., 3:] = src[..., 3:]
     # チャンネル分解
    r, g, b = src[:,:,0], src[:,:,1], src[:,:,2]
    maxc = np.max(src[..., :3], axis=-1)
    minc = np.min(src[..., :3], axis=-1)
    hsv[:,:,2] = maxc
    mask = maxc != minc
    hsv[mask, 1] = (maxc - minc)[mask] / maxc[mask]
    rc = np.zeros_like(r)
    gc = np.zeros_like(g)
    bc = np.zeros_like(b)
    rc[mask] = (maxc - r)[mask] / (maxc - minc)[mask]
    gc[mask] = (maxc - g)[mask] / (maxc - minc)[mask]
    bc[mask] = (maxc - b)[mask] / (maxc - minc)[mask]
    hsv[:,:,0] = np.select(
        [r == maxc, g == maxc], [bc - gc, 2.0 + rc - bc], default=4.0 + gc - rc)
    hsv[:,:,0] = (hsv[:,:,0] / 6.0) % 1.0
    return hsv 
    
def main():
    # 入力画像の読み込み
    img = cv2.imread("input.jpg")

    # 方法1
    hsv1 = rgb_to_hsv(img)
    
    # 方法2       
    hsv2 = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    
    # 結果を出力
    cv2.imwrite("hsv1.jpg", hsv1)
    cv2.imwrite("hsv2.jpg", hsv2)
    
if __name__ == "__main__":
    main()
