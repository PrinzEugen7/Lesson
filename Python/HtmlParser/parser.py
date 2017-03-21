# -*- coding: utf-8
import urllib
import html.parser as hp

# HTMLParserを継承したクラスを定義
class Parser(hp.HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("START :", tag, attrs)
    def handle_endtag(self, tag):
        print("END :", tag)
    def handle_data(self, data):
        print("DATA:", data)
    def handle_comment(self, comment):
        print("COMMENT:", comment)

def main():
    # 取得先URL
    url = "https://algorithm.joho.info/" 
 
    # HTMLファイルを開く
    data = urllib.request.urlopen(url)
    
    # HTMLの取得      
    html = data.read()
    html = html.decode('utf-8')

    # HTML解析(タイトルタグの値取得)     
    parser = Parser()
    parser.feed(html)
    
    # 終了処理
    parser.close()
    data.close()

    
if __name__ == "__main__":
    main()
