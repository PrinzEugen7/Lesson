# -*- coding: utf-8 -*-
import ftplib

def main():
    # 接続先サーバーのホスト名
    ftp = ftplib.FTP("xxx.xxx.xxx")
    ftp.set_pasv("true")
    # ユーザ名とパスワードを指定しログイン
    ftp.login("user", "password")
    # アップロードするファイル
    fp = open("test.csv", 'rb')
    # アップロード先のディレクトリ
    ftp.storbinary("STOR /sample/test.csv",fp)
    # 終了処理
    ftp.close()
    fp.close()

if __name__=='__main__':
    main()
