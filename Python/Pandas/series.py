# -*- coding: utf-8 -*-
import pandas as pd

def main():
    # 1次元配列
    data = pd.Series([158, 157, 157], index=['miho','saori','yukari'])
    print(data)

if __name__ == "__main__":
    main()
