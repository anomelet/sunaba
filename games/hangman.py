# -*- cording: utf-8 -*-
import random
import urllib.request
from bs4 import BeautifulSoup

def game():
    wrong = 0
    word = random_word()
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
    tango = []
    url = "https://ejje.weblio.jp/ranking/dictionary/wehgj"
    html = urllib.request.urlopen(url)
        # htmlをBeautifulSoupで扱う
    soup = BeautifulSoup(html,"html.parser")
        # span要素すべてを摘出する
    a = soup.find_all("a")
    for tag in a:
        try:
            string_ = tag.get("title").pop(0)
            if str.isalpha(string_):
                tango.append(string_)
        except:
            # 処理は行わず
            pass
    return tango

print(scrape_word())
