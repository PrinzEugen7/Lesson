# -*- coding: utf-8 -*-
import datetime as dt

def main():
    date = dt.datetime(2017, 5, 3, 12, 00, 00)
    date = date + dt.timedelta(days=5, hours=1, minutes=30)
    print(date) # 2017-05-08 13:30:00
    
if __name__=='__main__':
    main()
