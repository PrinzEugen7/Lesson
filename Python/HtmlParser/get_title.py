# -*- coding: utf-8
import urllib
import html.parser as hp

# HTMLParserを継承したクラスを定義
class ParserTitle(hp.HTMLParser):
    # コンストラクタ
    def __init__(self):
        hp.HTMLParser.__init__(self)
        self.title_flag = False # タイトルタグのフラグ
 
    def handle_starttag(self, tag, attrs): # 開始タグを扱うメソッド
        if tag == "title":
            self.title_flag = True
 
    def handle_data(self, data): # 要素内のデータを扱うメソッド
        if self.title_flag:
            self.title = data
            self.title_flag = False
 
def main():
    # 取得先URL
    url = "https://algorithm.joho.info/" 
 
    # HTMLファイルを開く
    data = urllib.request.urlopen(url)
    
    # HTMLの取得      
    html = data.read()
    html = html.decode('utf-8')

    # HTML解析(タイトルタグの値取得)     
    parser = ParserTitle()        # パーサオブジェクトの生成
    parser.feed(html) # パーサにHTMLを入力する
    
    # タイトルタグの中身表示
    print('Title:', parser.title)
    
    # 終了処理
    parser.close()
    data.close()

    
if __name__ == "__main__":
    main()
