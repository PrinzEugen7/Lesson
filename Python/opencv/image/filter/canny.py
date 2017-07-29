#-*- coding:utf-8 -*-
import cv2
import numpy as np

# 畳み込み演算（空間フィルタリング）
def filter2d(src, kernel, fill_value=-1):
    # カーネルサイズ
    m, n = kernel.shape
    
    # 畳み込み演算をしない領域の幅
    d = int((m-1)/2)
    h, w = src.shape[0], src.shape[1]
    
    # 出力画像用の配列を初期化
    if fill_value == -1: dst = src.copy() # 要素を入力画像と同じにする
    elif fill_value == 0: dst = np.zeros((h, w)) # 要素を0にする
    else: # 要素を指定した値で埋める
        dst = np.zeros((h, w))
        dst.fill(fill_value)
    
    for y in range(d, h - d):
        for x in range(d, w - d):
            # 畳み込み演算
            #print(x, y)
            #print(src[y-d:y+d+1, x-d:x+d+1])
            dst[y][x] = np.sum(src[y-d:y+d+1, x-d:x+d+1]*kernel)
            
    return dst

# Non maximum Suppression処理
def non_max_sup(G, Gth):

    width, height = G.shape
    dst = G.copy()

    # 注目画素と勾配方向に隣接する2つの画素値を比較し、注目画素値が最大でなければ0に
    for x in range(1, width-1):
        for y in range(1, height-1):
            if Gth[x][y]==0:
                if (G[x][y]<=G[x][y+1]) or (G[x][y]<=G[x][y-1]):
                    dst[x][y]=0
            elif Gth[x][y]==45:
                if (G[x][y]<=G[x-1][y+1]) or (G[x][y]<=G[x+1][y-1]):
                    dst[x][y]=0
            elif Gth[x][y]==90:
                if (G[x][y]<=G[x+1][y]) or (G[x][y]<=G[x-1][y]):
                    dst[x][y]=0
            else:
                if (G[x][y]<=G[x+1][y+1]) or  (G[x][y]<=G[x-1][y-1]):
                    dst[x][y]=0
    return dst

def traverse(i, j, gnh, gnl):
    x = [-1, 0, 1, -1, 1, -1, 0, 1]
    y = [-1, -1, -1, 0, 0, 1, 1, 1]
    for k in range(8):
        if gnh[i+x[k]][j+y[k]] == 0 and gnl[i+x[k]][j+y[k]] != 0:
            gnh[i+x[k]][j+y[k]] = 255
            traverse(i+x[k], j+y[k], gnh, gnl)

# Hysteresis Threshold処理
def hysteresis_threshold(G, t_min=75, t_max=150):

    w, h = G.shape
    gnh = np.zeros((w, h))
    gnl = np.zeros((w, h))

    for x in range(w):
        for y in range(h):
            # 最大閾値より大きければ信頼性の高い輪郭
            if G[x][y] >= t_max: gnh[x][y] = G[x][y]
            # 最小閾値～最大閾値の中間なら輪郭候補
            if G[x][y] >= t_min: gnl[x][y] = G[x][y]

    gnl = gnl - gnh

    for i in range(1, w-1):
        for j in range(1, h-1):
            if gnh[i][j]:
                gnh[i][j] = 255
                traverse(i, j, gnh, gnl)
    return gnh

def canny_edge_detecter(gray, t_min, t_max):


    # 処理1 ガウシアンフィルタで平滑化      
    kernel_g = np.array([[1/16, 1/8, 1/16],
                         [1/8,  1/4,  1/8],
                         [1/16, 1/8, 1/16]])
                         
    G = filter2d(gray, kernel_g, -1)

    # 処理2 微分画像の作成（Sobelフィルタ）
    kernel_sx = np.array([[-1,0,1],
                          [-2,0,2],
                          [-1,0,1]])
                          
    kernel_sy =  np.array([[-1,-2,-1],
                           [0,  0, 0],
                           [1,  2, 1]])
                           
    gradx = filter2d(G, kernel_sx, 0)
    grady = filter2d(G, kernel_sy, 0)
    
    # 処理3 勾配強度・方向を算出
    G = np.hypot(gradx, grady)
    Gth = np.arctan2(grady, gradx)

    # 勾配方向を4方向(垂直・水平・斜め右上・斜め左上)に近似
    Gth[np.where((Gth >= 0) & (Gth < 22.5))] = 0
    Gth[np.where((Gth >= 22.5) & (Gth < 67.5))] = 45
    Gth[np.where((Gth >= 67.5) & (Gth < 112.5))] = 90
    Gth[np.where((Gth >= 112.5) & (Gth < 157.5))] = 135
    Gth[np.where((Gth >= 157.5 ) & (Gth < 202.5))] = 0
    Gth[np.where((Gth >= 202.5 ) & (Gth < 247.5))] = 45
    Gth[np.where((Gth >= 247.5) & (Gth < 292.5))] = 90
    Gth[np.where((Gth >= 292.5) & (Gth < 337.5))] = 135
    Gth[np.where((Gth >= 337.5) & (Gth < 360))] = 0

    # 処理4 Non maximum Suppression処理
    G = non_max_sup(G, Gth)

    # 処理5 Hysteresis Threshold処理
    return hysteresis_threshold(G, t_min, t_max)


def main():
    # 入力画像を読み込み
    img = cv2.imread("input.jpg")

    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # 方法1（NumPyでCannyアルゴリズムを実装）
    edge1 = canny_edge_detecter(gray, t_min=100, t_max=200)
    
    # 方法2（OpenCVでCannyアルゴリズムを実装）
    edge2 = cv2.Canny(gray, 100, 200)

    # 結果を出力
    cv2.imwrite("output1.jpg", edge1)
    cv2.imwrite("output2.jpg", edge2)

    
if __name__ == "__main__":
    main()
