#-*- coding:utf-8 -*-
import json,os,sys,re,glob,urllib2
import cv2

def trim_face(keyword):

    if os.path.exists(keyword+"_trim")==False:
        os.mkdir(keyword+"_trim")

    for infn in os.listdir(keyword):
        fn, ext = os.path.splitext(infn)
        im = cv2.imread(keyword+"\\"+infn)
        cascade = cv2.CascadeClassifier("lbpcascade_animeface.xml")
        face = cascade.detectMultiScale(im, 1.1, 3)

        for (x, y, w, h) in face:
            im_trim = im[y:y+h, x:x+w]
            cv2.imwrite(keyword+"_trim\\"+fn+"["+str(x)+","+str(y)+"]"+ext,im_trim)



def url_search(keyword, n):

    img_url=[]
    url = "http://ajax.googleapis.com/ajax/services/search/images?q={0}&v=1.0&rsz=large&start={1}"

    for i in range((n/8)+1):
        res = urllib2.urlopen(url.format(keyword, i*8))
        data = json.load(res)
        img_url += [result["url"] for result in data["responseData"]["results"]]

    return img_url


def url_download(keyword,urls):

    if os.path.exists(keyword)==False:
        os.mkdir(keyword)

    opener = urllib2.build_opener()

    for i in range(len(set(urls))):
        try:
            fn, ext = os.path.splitext(urls[i])
            req = urllib2.Request(urls[i], headers={'User-Agent' : "Magic Browser"})
            img_file = open(keyword+"\\"+str(i)+ext, 'wb')
            img_file.write(opener.open(req).read())
            img_file.close()
            print "DL Image Link:"+str(i+1)
        except:
            continue


if __name__ == '__main__':

    keyword="nonnonbiyori"
    urls = url_search(keyword, n=1)

    print "[1/2]Download Start"
    url_download(keyword,urls)

    print "[2/2]Trimming Anime Face"
    trim_face(keyword)

    print "End..."
