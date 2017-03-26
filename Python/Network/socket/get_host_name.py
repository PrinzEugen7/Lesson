# -*- coding: utf-8 -*-
import socket
 
def main():
    host = socket.gethostname()
    print(host) # ホスト名
 
if __name__ == "__main__":
    main()
