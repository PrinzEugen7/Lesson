# -*- coding: utf-8 -*-
import pandas_datareader.data as web
import datetime

def main():
    start = datetime.datetime(2017, 2, 20)
    end = datetime.datetime(2017, 2, 22)
    f = web.DataReader('^N225', 'yahoo', start, end)
    print(f)


if __name__ == '__main__':
    main()
