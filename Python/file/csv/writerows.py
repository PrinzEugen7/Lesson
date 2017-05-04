# -*- coding: utf-8 -*-
import csv

def main():
# 内容
    data = [[0, 'YUI'],[1, 'UI'],[2, 'MIO']]

    with open('data.csv', 'w', newline='') as f:    #newline=''を追加した
        writer = csv.writer(f)
        writer.writerows(data)   

    f.close()

if __name__=='__main__':
    main()
