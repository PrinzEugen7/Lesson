# -*- coding: utf-8 -*-
import datetime as dt

def main():
    date = dt.datetime(2017, 1, 1, 0, 0)
    for i in range(365):
        print(date)
        date += dt.timedelta(days=1)

    
if __name__=='__main__':
    main()
