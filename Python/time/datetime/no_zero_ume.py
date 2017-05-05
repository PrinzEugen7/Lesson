import datetime as dt
 
def main():
    date = dt.datetime(2017, 1, 1, 0, 0)
    date = date.strftime('%Y-%-m-%-d %-H:%-M')
    print(date)
 
if __name__=='__main__':
    main()
