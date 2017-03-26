#-*- coding:utf-8 -*-
# api終了に伴い現在利用不可
import os
import urllib.parse
import urllib.request
import json
import random
import imghdr
import subprocess
 
def get_google_image(num, word):
    if len(word) <= 0:
      print('Usage:')
      print('python fetch_google_image.py cat cute')
      exit()   
    q = ''
     
    for arg in word:
      q += urllib.parse.quote(arg) + '+'
     
    f = urllib.request.urlopen('http://ajax.googleapis.com/ajax/services/search/images?q=' + q + '&v=1.0&rsz=small').read().decode('utf-8')
    data = json.loads(f)
     
    results = data['responseData']['results']
    url = results[0]['url']
    urllib.request.urlretrieve(url, './image/tmp')
     
    imagetype = imghdr.what('./image/tmp')
    if not(type(imagetype) is None):
        filename =  './image/{0:0>4}'.format(num) + '.' + imagetype
        os.rename('./image/tmp', filename)

    print("get imge num : {0}".format(num))
    print("get imge name : {0}".format(word))

if __name__ == '__main__':
    testword = ["猫"]
    get_google_image(0, testword)
