def NAND(a,b):
    if a==1 and b==1:
        return 0
    else:
        return 1

def NOT(a):
    return NAND(a,a)

def AND(a,b):
    return NAND(NAND(a,b),NAND(a,b))

def OR(a,b):
    return NAND(NAND(a,a),NAND(b,b))

def NOR(a,b):
    return NAND(NAND(NAND(a,a),NAND(b,b)),NAND(NAND(a,a),NAND(b,b)))

def SRFF(S,R,Q=0,BQ=0):
    if S == 1 and R == 1:
        print("SRFF can't input '1'and'1'.")
    else:
        Q = NOR(R,NOR(S,Q))
        BQ = NOR(S,Q)
    return Q,BQ

def DFF(D,T,Q=0,BQ=0):
    Q = NAND(NAND(D,T),NAND(Q,NAND(NAND(D,T),T)))
    BQ = NAND(Q,NAND(NAND(D,T),T))
    return Q,BQ

Q = 0
BQ = 0
while 1:
    S = input("S:")
    R = input("R:")

    (Q,BQ) = DFF(int(S),int(R),Q,BQ)
    print(S,R,Q,BQ)
