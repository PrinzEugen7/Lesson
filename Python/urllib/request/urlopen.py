# -*- coding: utf-8
import urllib
    
def main():
    # 取得先URL
    url = "https://algorithm.joho.info/" 
 
    # HTMLファイルを開く
    data = urllib.request.urlopen(url)

    # HTMLの取得      
    html = data.read()
    
    # 表示
    print(html)
    
    # HTMLファイルを閉じる
    data.close()
   
    
if __name__ == "__main__":
    main()
