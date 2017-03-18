# -*- coding: utf-8
import sqlite3

def main():
    # データベース開く
    db = sqlite3.connect('sarvant.db')
    c = db.cursor()
    
    # テーブル作成
    c.execute('create table artoria (name text, atk int, hp int)')

    # コミット
    db.commit()

    # クローズ
    db.close()

if __name__ == "__main__":
    main()
