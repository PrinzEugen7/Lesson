# -*- coding: utf-8 -*-
import urllib


def main():
    # グローバルIPアドレスを取得
    ip = urllib.request.urlopen('http://ipcheck.ieserver.net').read().decode('utf-8')

    print(ip) # グローバルIPアドレス


if __name__ == "__main__":
    main()
