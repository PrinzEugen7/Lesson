# -*- coding: utf-8 -*-
import sqlite3

def main():
    # DBに接続
    db = sqlite3.connect("sarvant.db")
    # テーブル作成
    sql = "create table artoria (name varchar, class varchar, atk integer, hp integer, rank varchar);"
    db.execute(sql)
    # レコード登録（データ追加）
    db.execute("insert into artoria values ('artoria','saver','11221','15150','5')")
    db.execute("insert into artoria values ('artoria alter','saver','10248','11589','4')")
    db.execute("insert into artoria values ('artoria lily','savar','7726','10623','4')")
    db.execute("insert into artoria values ('artoria lancer','lancer','10995','15606','5')")
    db.execute("insert into artoria values ('artoria lancer alter','lancer','9968','11761','4')")
    db.execute("insert into artoria values ('artoria swimwear','archer','11276','14553','5')")
    db.execute("insert into artoria values ('artoria santa alter','rider','9258','11286','4')")
    db.execute("insert into artoria values ('mystery heroine x','assassin','11761','12696,'5')")
    db.execute("insert into artoria values ('mystery heroine x alter','berserker','11113','14175','5')")
    # 処理実行
    db.commit()
    # DB閉じる
    db.close()

if __name__ == "__main__":
    main()
