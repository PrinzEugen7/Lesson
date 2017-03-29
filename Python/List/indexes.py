#-*- coding:utf-8 -*-

def main():
    list = [1,2,3,4,5,4,3,2,1]
    indexes = [i for i, e in enumerate(list) if e == 3]
    print(indexes) # [2, 6]
    
if __name__ == "__main__":
    main()
