# -*- coding: utf-8
import numpy as np

def main():
    # CSVのロード
    data = np.genfromtxt("nikkei.csv",delimiter=",", skip_header=1, dtype='float')
    # 結果表示
    print(data)

if __name__ == "__main__":
    main()
