# -*- cording: utf-8 -*-
from gates import NAND

class auto_NAND:

    def __init__(self,inputs,outputs):
        """ inputs(入力の数)とoutputs[](出力の01)を受け取る """
        self.ins = inputs
        self.table = []
        self.outs = outputs
        print (self.make_table(inputs))
                

    def make_table(self,inputs):
        """ 入力の要素から、出力が空の真理値表を作成
            入力の要素ずつ追加、次の要素で再帰する　 """
        
        # 再帰を抜けるための条件
        if inputs == 0:　　　　　#要素が最後まで行ったら
            return self.table

        # 要素の列を作成
        statetable = []
        for i in range(0,2**(self.ins-inputs)):     # 繰り返す回数を変更します
            for boo in range(0,2):                  # 0と1で繰り返します
                for ins in range(0,2**(inputs-1)):  # 0と1を何個ずつ置くか決めます
                    statetable.append(boo)

        self.table.append(statetable) # 要素を真理値表に追加
        return self.make_table(inputs-1)

    def make_fomula(self,inputs,outputs):
        """ 真理値表から論理式を出力します。 """
        tlen = 2**(inputs)
        fomu = []
        if tlen != len(outputs):
            print("入出力の状態数が一致しません!")
            return None

        for y in range(0,tlen):
            if outputs[y] == 1:
                fomu.append()
            else:
                pass

        

auto_NAND(3)
