# -*- coding: utf-8 -*-
import csv

def main():
    f = open('data.csv', 'w')
    writer = csv.writer(f, lineterminator='\n')
    data = ["YUI", 50]
    writer.writerow(data)
    f.close()
    
if __name__=='__main__':
    main()
