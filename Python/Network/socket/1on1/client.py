# -*- coding: utf-8 -*-
import socket

def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect(("localhost", 50007))

    while(1):
        data = soc.recv(1024)
        print("Server>", data)      # サーバー側の書き込みを表示
        data = input("Client>") # 入力待機
        soc.send(data)              # ソケットに入力したデータを送信

        if data == "q":             # qが押されたら終了
            soc.close()
            break

if __name__ == '__main__':
    main()
