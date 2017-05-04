# -*- coding: utf-8 -*-
import csv
import datetime as dt

def get_dates():
    date = dt.datetime(2017, 1, 1, 0, 0)
    dates = []
    for i in range(365*24):
        dates.append(date.strftime('%Y-%m-%d %-H:%M'))
        date += dt.timedelta(hours=1)
    return dates

def write_csv(data):
   with open('data.csv', 'w', newline='') as f:    #newline=''を追加した
        writer = csv.writer(f)
        writer.writerows(data)   

   f.close()
    
def main():
    dates = get_dates()
    temps = [0]*365*24
    humids = [0]*365*24
    presss = [0]*365*24
    pm25s = [0]*365*24
    data = [dates, temps, humids, presss, pm25s]
    data = list(map(list, zip(*data)))
    print(data)
    write_csv(data)
    
if __name__=='__main__':
    main()
