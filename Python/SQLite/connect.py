# -*- coding: utf-8 -*-
import sqlite3

def main():
    # DBに接続
    db = sqlite3.connect("sarvant.db")
    # DB閉じる
    db.close()

if __name__ == "__main__":
    main()
