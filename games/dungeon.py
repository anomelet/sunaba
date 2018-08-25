# -*- cording: utf-8 -*-

class dungeon:
    def __init__(self):
        self.selectSeane("T")

    def seaneSelecter(self,key):
        while True:
            if key == "T":
                key = topMenu()
            if key == "S":
                key = 

    def topMenu(self):
        title = ["############################################",
                 "                                            ",
                 "############################################",
                 "###                                         ",
                 "#   #                                       ",
                 "#    # #   # # ###   ### # ###   ###  # ### ",
                 "#    # #   #  #   # #   # #   # #   #  #   #",
                 "#    # #   #  #   # #   # ##### #   #  #   #",
                 "#   #  #   #  #   # #   # #     #   #  #   #",
                 "###     ### # #   #  ####  ###   ###   #   #",
                 "                        #                   ",
                 "                    #   #                   ",
                 "                     ###                    ",
                 "############################################",]
        print("\n".join(title))
        while True:
            key = input("[S]tart or [Q]uit :")
            if key == "S" or key == "Q":
                return key

dungeon.topMenu("a")
