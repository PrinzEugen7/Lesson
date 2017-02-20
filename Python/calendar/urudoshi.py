# -*- coding: utf-8 -*-
import calendar

def main():
    # うるう年の探索
    for year in range(2001, 2020):
        # うるう年の判定
        if(calendar.isleap(year) == True):
            print(year, "年はうるう年です。")

    print("うるう年の回数:", calendar.leapdays(2001, 2020))

if __name__ == "__main__":
    main()
