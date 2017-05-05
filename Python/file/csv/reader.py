# -*- coding: utf-8 -*-
import csv

def main():
    f = open("data.csv", "r")
    csv_data = csv.reader(f)
    data = [ e for e in csv_data]
    print(data)
    f.close()
    
if __name__=='__main__':
    main()
