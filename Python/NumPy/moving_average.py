# -*- coding: utf-8
import numpy as np
    
def main():
    # 移動平均の点数
    n = 3
    
    # 配列生成
    data = np.array([ 1,  2,  5,  4,  2,  4,  3])
    
    # コンボリューション積分で移動平均の計算
    ave = np.convolve(data, np.ones(n)/float(n), 'valid')
    
    # 結果表示
    print(ave) # [ 2.66666667  3.66666667  3.66666667  3.33333333  3.]
    
if __name__ == "__main__":
    main()
