# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        self.site = "https://news.google.com/"
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)

    def scrape_Nikkei(self):
        url = "http://www.nikkei.com/markets/kabu/" #アクセスするURL
        # URLにアクセスする　htmlが帰ってくる
        html = urllib.request.urlopen(url)
        # htmlをBeautifulSoupで扱う
        soup = BeautifulSoup(html,"html.parser")
        # span要素すべてを摘出する
        span = soup.find_all("span")

        nikkei_heikin = ""
        for tag in span:
            try:
                string_ = tag.get("class").pop(0)
                if string_ in "mkc-stock_prices":
                    nikkei_heikin = tag.string
                    break
            except:
                # 処理は行わず
                pass

        # タイトルを文字列を出力
        print(soup.title.string)
        # 日経平均出力
        print("日経平均：",nikkei_heikin)

    def scrape_Nintendo(self):
        url = "http://www.nikkei.com/markets/kabu/" #アクセスするURL
        # URLにアクセスする　htmlが帰ってくる
        html = urllib.request.urlopen(url)
        # htmlをBeautifulSoupで扱う
        soup = BeautifulSoup(html,"html.parser")
        # span要素すべてを摘出する
        span = soup.find_all("span")

        nikkei_heikin = ""
        for tag in span:
            try:
                string_ = tag.get("class").pop(0)
                if string_ in "mkc-stock_prices":
                    nikkei_heikin = tag.string
                    break
            except:
                # 処理は行わず
                pass

        # タイトルを文字列を出力
        print(soup.title.string)
        # 日経平均出力
        print("日経平均：",nikkei_heikin)

Scraper("s").scrape_Nikkei()



