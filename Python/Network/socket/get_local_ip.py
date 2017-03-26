# -*- coding: utf-8 -*-
import socket


def main():
    # ローカルIPアドレスを取得
    ip = socket.gethostbyname(socket.gethostname())
    print(ip) # 192.168.○○○.○○○
    
if __name__ == "__main__":
    main()
