# -*- coding: utf-8
import numpy as np

    
def main():
    # 配列生成
    A = np.array([0, 1, 1, 1, 2, 0, 0])
    
    # 0の要素数　= 全要素数 - 0でない要素数
    num = len(A) - np.count_nonzero(A)
    
    # 結果表示
    print(num) # 3
   
    
if __name__ == "__main__":
    main()
