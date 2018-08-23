# -*- cording: utf-8 -*-
import random
import re
import urllib.request
from bs4 import BeautifulSoup

def game(word):
    wrong = 0
    rletters = list(word)
    win = False
    board = ["_"] * len(word)
    stages = ["",
              "__________      ",
              "||        |     ",
              "||        O     ",
              "||       /|\    ",
              "||       / \    ",
              "||\      ___    ",
              ]
    print("ハングマンへようこそ！")
    while wrong < len(stages):
        print("\n")
        char = input("1文字予想してね :")
        if char in rletters:
            num = rletters.index(char)
            board[num] = char
            rletters[num] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け。正解は{}.".format(word))

def random_word():
    words = ["cat",
             "snow",
             "smile",
             "dog",
             "boom",
             "red"
             ]
    return words[random.randrange(len(words))]

def scrape_word():
    """ 本日のランキング上位５０から、半角小文字のみの単語をランダムで出力 """
    print("準備中だよ。ちょっと待ってね。")
    
    lowerReg = re.compile(r'^[a-z]+$') # 正規表現：半角小文字のみ
    tango = []
    url = "https://ejje.weblio.jp/ranking/dictionary/wehgj"
    html = urllib.request.urlopen(url)
        # htmlをBeautifulSoupで扱う
    soup = BeautifulSoup(html,"html.parser")
        # span要素すべてを摘出する
    a = soup.find_all("a",href = re.compile("https://ejje.weblio.jp/content/"))

    for tag in a:
        try:
            string_ = tag.get("title")
            if lowerReg.match(string_) is not None:
                tango.append(string_)
        except:
            # 処理は行わず
            pass
    return tango

def loop_games():
    tango = scrape_word()
    while True:
        inp = input("終わるなら[q]を押してね。それ以外は続行！！ :")
        if (inp == "q"):
            return
        game(tango[random.randrange(len(tango))])
        
loop_games()
