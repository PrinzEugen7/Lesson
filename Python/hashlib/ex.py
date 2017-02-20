# -*- coding: utf-8 -*-
import hashlib

def main():
    # 文字列
    message = "nyanpasu"
    # ハッシュ値を求めた結果
    print("MD5:", hashlib.md5(message).hexdigest() )
    print("sha256:", hashlib.sha256(message).hexdigest() )
    print("sha516:", hashlib.sha512(message).hexdigest() )

if __name__ == "__main__":
    main()
