# -*- coding: utf-8 -*-
import sqlite3

def main():
    # DBに接続
    db = sqlite3.connect("sarvant.db")
    sql = """
    create table artoria (
                 name varchar,
                 class varchar,
                 atk integer,
                 hp integer,
                 rank varchar);
   """
    db.execute(sql)
    # DB閉じる
    db.commit()
    db.close()

if __name__ == "__main__":
    main()
