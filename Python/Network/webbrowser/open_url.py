# -*- coding: utf-8 -*-
import webbrowser


def main():
    url = "http://www.nicovideo.jp/"
    browser = webbrowser.get('"c:\\program files\\internet explorer\\iexplore.exe" %s')
    browser.open(url)

if __name__ == "__main__":
    main()
