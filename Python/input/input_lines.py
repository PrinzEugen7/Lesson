#-*- coding:utf-8 -*-

def main():
    # 行数を取得
    num_lines = int(input())
    
    # 1行ずつ取り出し
    for i in range(num_lines):
        line = input()
        print(i+1, "行目:" + line)
    
if __name__ == "__main__":
    main()
