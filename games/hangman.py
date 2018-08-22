# -*- cording: utf-8 -*-
import random

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

game()
