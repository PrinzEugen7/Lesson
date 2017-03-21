# -*- coding: utf-8
import urllib
import html.parser as hp

# HTMLParserを継承したクラスを定義
class ParserTag(hp.HTMLParser):
 
    def __init__(self, target):
        hp.HTMLParser.__init__(self)
        self.flag = False    # タグが見つかったかのフラグ
        self.target = target # 目標タグ
        
    # 開始タグを扱うメソッド  
    def handle_starttag(self, tag, attrs): 
        # 目標タグが見つかったら
        if tag == self.target:
            self.flag = True
            
    # タグ内のデータを扱うメソッド
    def handle_data(self, data): 
        # 目標タグが見つかれば
        if self.flag:
            self.data = data
            self.flag = False
 
def main():
    # 取得先URL
    url = "https://algorithm.joho.info/" 
 
    # HTMLファイルを開く
    data = urllib.request.urlopen(url)
    
    # HTMLの取得      
    html = data.read()
    html = html.decode('utf-8')

    # HTML解析(タイトルタグの値取得)     
    parser = ParserTag('title')
    parser.feed(html)
    
    # タイトルタグの中身表示
    print('Title:', parser.data) # Title: アルゴリズム速報
    
    # 終了処理
    parser.close()
    data.close()

    
if __name__ == "__main__":
    main()
