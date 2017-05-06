# -*- coding: utf-8 -*-
import csv

def read_csv(filename):
    f = open(filename, "r")
    csv_data = csv.reader(f)
    list = [ e for e in csv_data]
    f.close()
    return list
    
def update_list2d(list, data):
    for i in range(len(list)):
        if list[i][0]==data[0]: list[i] = data
    return list

def write_csv(filename, list):
   with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(list)   

   f.close()

def main():
    filename = 'data.csv'
    csv_data = read_csv(filename)
    data = ["2017-01-01 01:00", 20, 50, 1030, 5]
    csv_data2 = update_list2d(csv_data, data)
    write_csv(filename, csv_data2)
    
if __name__=='__main__':
    main()
