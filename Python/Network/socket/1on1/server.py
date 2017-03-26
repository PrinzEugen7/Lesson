# -*- coding: utf-8 -*-
import socket

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", 50007))    # 指定したホスト(IP)とポートをソケットに設定
    s.listen(1)                     # 1つの接続要求を待つ
    soc, addr = s.accept()          # 要求が来るまでブロック
    print("Conneted by"+str(addr))  #サーバ側の合図

    while (1):
        data = raw_input("Server>") # 入力待機(サーバー側)
        soc.send(data)              # ソケットにデータを送信
        data = soc.recv(1024)       # データを受信（1024バイトまで）
        print "Client>",data        # サーバー側の書き込みを表示
        if data == "q":             # qが押されたら終了
            soc.close()
            break

if __name__ == '__main__':
    main()
