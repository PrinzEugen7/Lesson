# -*- coding: utf-8 -*-

def main():

    for i in range(5):
        # iが3の時だけスルー
        if(i == 3):
            continue

        print(i)

if __name__ == "__main__":
    main()
