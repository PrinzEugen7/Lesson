#-*- coding:utf-8 -*-
import sys

def main():
    # 行数を取得
    lines = sys.stdin.readlines()
    
    # 中身表示
    print(lines) # ['沖田\n', 'モードレッド']
    
    # 1行ずつ取り出し
    for i, line in enumerate(lines):
    	# 改行コードが含まれていれば除去
        line = line.strip("\n")
        print(i+1, "行目:", line)
    
if __name__ == "__main__":
    main()
