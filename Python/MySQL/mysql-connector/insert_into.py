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
    rows = db.fetchall()

    # 表示
    print(rows)

    # カーソル終了
    db.close()
    # MySQL切断
    cnt.close()

if __name__ == "__main__":
    main()
