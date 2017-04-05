#-*- coding:utf-8 -*-
from urllib.parse import urlparse
import urllib.request

def main():
    url = 'https://twitter.com/search?q=進撃の巨人'
    p = urlparse(url)
    query = urllib.parse.quote_plus(p.query, safe='=&')
    url = '{}://{}{}{}{}{}{}{}{}'.format(
        p.scheme, p.netloc, p.path,
        ';' if p.params else '', p.params,
        '?' if p.query else '', query,
        '#' if p.fragment else '', p.fragment)
    response = urllib.request.urlopen(url)
    
if __name__ == '__main__':
    main()
