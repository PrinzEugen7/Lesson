# -*- coding: utf-8 -*-
import mysql.connector

def main():
    # MySQL接続
    cnt = mysql.connector.connect(
        host='localhost',
        port='3306',
        db='sarvant',
        user='root',
        password='password',
        charset='utf8'
    )

    # カーソル取得
    db = cnt.cursor(buffered=True)

    # SQLクエリ実行（データ追加）
    sql = 'INSERT INTO artoria(name) VALUES("nero claudius")';
    db.execute(sql)
    
    # SQLクエリ実行（データ取得）
    sql = 'SELECT name FROM artoria';
    db.execute(sql)
    
    # 表示
    rows = db.fetchall()
    print(rows)

    # カーソル終了
    db.close()
    # MySQL切断
    cnt.close()

if __name__ == "__main__":
    main()
