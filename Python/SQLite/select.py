# -*- coding: utf-8 -*-
import sqlite3

def main():
    # DBに接続
    db = sqlite3.connect("sarvant.db")
    c = db.cursor()
    c.execute("select name from artoria")
    print(c)
    # 処理実行
    db.commit()
    # DB閉じる
    db.close()

if __name__ == "__main__":
    main()
