#-*- coding:utf-8 -*-
import json
import os
import urllib2

# keywordの画像リンクを探索
def url_search(keyword, n):

    img_url=[]
    url = "http://ajax.googleapis.com/ajax/services/search/images?q={0}&amp;v=1.0&amp;rsz=large&amp;start={1}"
    # keywordと一致する画像URLをn個取得
    for i in range((n/8)+1):
        res = urllib2.urlopen(url.format(keyword, i*8))
        data = json.load(res)
        img_url += [result["url"] for result in data["responseData"]["results"]]

    return img_url

# URL先の画像ファイルを保存
def url_download(keyword,urls):
    print("Download Start...")
    # keywordのフォルダが無ければ作成
    if os.path.exists(keyword)==False:
        os.mkdir(keyword)

    opener = urllib2.build_opener()
    # URLの数だけ画像DL
    for i in range(len(set(urls))):
        try:
            fn, ext = os.path.splitext(urls[i])
            req = urllib2.Request(urls[i], headers={"User-Agent" : "Magic Browser"})
            img_file = open(keyword+"\\"+str(i)+ext, "wb")  # 画像データの保存
            img_file.write(opener.open(req).read())
            img_file.close()
            print("DL Image Link:"+str(i+1))
        except:
            continue

# メイン文
def main():

    keyword = "kankore"         # 検索キーワード
    urls = url_search(keyword, n=1)     # 画像URLの探索
    url_download(keyword,urls)          # 画像のダウンロード
    print("End...")


if __name__ == '__main__':
    main()
