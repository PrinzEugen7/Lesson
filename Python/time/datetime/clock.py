# -*- coding: utf-8 -*-
import os
import datetime

def main():
    date_old = ""
    while(1):
        dt = datetime.datetime.now()
        date = dt.strftime('%Y-%m-%d %H:%M:%S')
        if date != date_old:
            os.system('cls')
            print(date)
        date_old = date      
        

if __name__ == "__main__":
    main()
