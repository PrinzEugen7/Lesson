# -*- coding: utf-8
import numpy as np

    
def main():
    # 配列生成
    A = np.array([0, 1, 1, 1, 2, 0, 0])
    
    # 値が2の要素数
    num =  len(np.where(A==1)[0])
    
    # 結果表示
    print(num) # 3
   
    
if __name__ == "__main__":
    main()
