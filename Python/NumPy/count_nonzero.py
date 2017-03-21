# -*- coding: utf-8
import numpy as np

    
def main():
    # 配列生成
    A = np.array([0, 1, 1, 1, 0, 0])
    
    # 要素が0の個数をカウント
    num = np.count_nonzero(A)
    
    # 結果表示
    print(num) # 3
   
    
if __name__ == "__main__":
    main()
