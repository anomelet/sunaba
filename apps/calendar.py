# -*- cording: utf-8 -*-
import tkinter as tk
import datetime

class calendar:
    def __init__(self):

        # 日付を取得
        now = datetime.datetime.now()
        # 現在の年と月を属性に追加
        self.year = now.year
        self.month = now.month

        frame_top = tk.Frame(self)
