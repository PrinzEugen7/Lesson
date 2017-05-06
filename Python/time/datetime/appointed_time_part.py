# -*- coding: utf-8 -*-
import datetime
import time

def main():
    while(1):
        dt = datetime.datetime.now()
        if str(dt.second) == "0":
            print(dt)
            time.sleep(1)
        time.sleep(0.1)
 
if __name__ == "__main__":
    main()
