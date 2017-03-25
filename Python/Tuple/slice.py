# -*- coding: utf-8 -*-

def main():
	# タプルの生成
    data = (1, 2, 3, 4, 5)
    # 表示
    print(data[1:3]) # (2, 3)
    print(data[1:])  # (2, 3, 4, 5)
    print(data[:2])  # (1, 2)
    
if __name__ == '__main__':
    main()
