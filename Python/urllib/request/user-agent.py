# -*- coding: utf-8
import urllib
    
def main():
    # 取得先URL
    url = "https://algorithm.joho.info/" 

    # ユーザーエージェント情報を設定
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; ja; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)')]

    # HTMLファイルを開く
    data = opener.open(url)
    
    # HTMLの取得      
    html = data.read()
    html = html.decode('utf-8')
    
    # 表示
    print(html)
    
    # HTMLファイルを閉じる
    data.close()
   
    
if __name__ == "__main__":
    main()
