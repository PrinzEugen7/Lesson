# -*- coding: utf-8
import numpy as np

# 平滑化処理(サンプル, カットオフ周波数)
def smooth(f, fc=0.1):
    # サンプル数 
    N = len(f)

    # 高速フーリエ変換
    F = np.fft.fft(f)/(N/2)
    
    # 周波数軸の値を計算 
    freq = np.fft.fftfreq(len(f))
    
    # 直流成分の振幅を揃える
    F[0] = F[0]/2
    
    # ローパス処理(平滑化)
    F[(freq > fc)] = 0
    F[(freq < 0)] = 0
    
    # 高速逆フーリエ変換
    f2 = np.fft.ifft(F)*(2*N/2)
    
    # 勾配を計算
    df2 = np.gradient(f2)

    # 3値化(前日の終値よりプラス:1, 変化なし:0, マイナス:-1)
    df2[df2 > 0] = 1
    df2[df2 == 0] = 0
    df2[df2 < 0] = -1

    return f2, df2
    
    
def main():
    # CSVのロード(2015年と2016年のデータ)
    data15 = np.genfromtxt("nikkei15.csv", delimiter=",", skip_header=1, dtype='float')
    data16 = np.genfromtxt("nikkei16.csv", delimiter=",", skip_header=1, dtype='float')
    
    # 5列目の終値だけを古い順に並び替えて取り出し
    f15, f16 = data15[:,4]/1000.0, data16[:,4]/1000.0
    f15, f16 = f15[::-1], f16[::-1]
    
    # 平滑化
    f15, df15 = smooth(f15, fc=0.1)
    f16, df16 = smooth(f16, fc=0.1)
    
    # 差分を計算
    result = df15 - df16
    
    # 差分が0(当たり)の個数を計算
    hit = len(result) - np.count_nonzero(result)
    
    # 当たりの確率をパーセント表示
    score = 100*hit/len(result)
    print(round(score, 3), "[%]")
    
    
if __name__ == "__main__":
    main()
