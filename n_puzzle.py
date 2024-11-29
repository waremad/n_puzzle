"""
整数を分数に変換
- 分数の四則
分数文字列をリスト型に
約分
加算 通分して足す
減算 通分して引く
乗算 分母分子同士をかけて、分母が負なら分母子にマイナス1かける
除算 割る数を逆数にして乗算
"""

def int2frac(self):#int型を分数を表すstr型に
    if self == "":
        return "0/1"
    out = str(self) + "/1"
    return out

def str2frac(self):#/区切りのstr型をlistに
    if self == "":
        return [0,1]
    out = self.split("/")
    for i in range(len(out)):
        out[i] = int(out[i])
    return out

def redufrac(self):#約分
    if self == "" or self[0] == "0" or self[:2] == "-0" or self[-1] == "0" or self[-2:] == "-0":
        return "0/1"
    self = str2frac(self)
    if self[0] < 0:
        minus = self[1] > 0
    else:
        minus = self[1] < 0
    for i in range(len(self)):
        self[i] = abs(self[i])
    n = min(self)
    while not(n == 1 or self[0]%n + self[1]%n == 0):
        n -= 1
    out = str(self[0]//n) + "/" + str(self[1]//n)
    if minus :
        out = "-" + out
    return out

def addfrac(self,self2):#分数の足し算
    self = str2frac(self)
    self2 = str2frac(self2)
    out = [
        self[0] * self2[1] + self[1] * self2[0],
        self[1] * self2[1]]
    for i in range(len(out)):
        out[i] = str(out[i])
    out = "/".join(out)
    out = redufrac(out)
    return out

def mulfrac(self,self2):#分数の掛け算
    self = str2frac(self)
    self2 = str2frac(self2)
    out = [
        self[0] * self2[0],
        self[1] * self2[1]]
    for i in range(len(out)):
        out[i] = str(out[i])
    out = "/".join(out)
    out = redufrac(out)
    return out

def subfrac(self,self2):#分数の引き算
    self2 = mulfrac(self2,"-1/1")
    return addfrac(self,self2)

def divfrac(self,self2):#分数の割り算
    self2 = str2frac(self2)
    self2[0], self2[1] = self2[1], self2[0]
    for i in range(len(self2)):
        self2[i] = str(self2[i])
    self2 = "/".join(self2)
    return mulfrac(self,self2)

"""
手順を示したlist[[0,0,0],[0,0,0]]
式を示したlist
値を示したlist

0 +
1 -
2 ×
3 ÷
"""

def action(n,sign,value,log):#１手進める
    sls = ["+","-","×","÷"]
    self1 = value.pop(n[0])
    log1 = log.pop(n[0])
    self2 = value.pop(n[1])
    log2 = log.pop(n[1])

    if sign == sls[0]:
        out = addfrac(self1,self2)
    elif sign == sls[1]:
        out = subfrac(self1,self2)
    elif sign == sls[2]:
        out = mulfrac(self1,self2)
    elif sign == sls[3]:
        out = divfrac(self1,self2)
    else:
        return "??action??","??action??"
    
    value.append(out)
    out = "(" + log1 + " " + sign + " " + log2 + ")"
    log.append(out)

    return (value,log)

par = 0
def onehand(hand=[],D=0):#手順listを１つ進める
    global par
    n = len(hand) - 1
    p = [0,0]
    do = True
    if p == [len(hand),0]:
            return "end"
    while do:
        if p[1] == 0:
            if hand[p[0]][0] == 3:
                hand[p[0]][0] = 0
                p[1] += 1
            else:
                hand[p[0]][0] += 1
                #"""
                if D < 500:
                    for i in hand:
                        if i[0] == 0 or i[0] == 2:
                            if i[1] <= i[2]:
                                rpar = 0
                                for j in hand:
                                    rpar += sum(j)
                                if rpar > par:
                                    par = rpar
                                    print(par*100//(len(hand)**2 + 3*len(hand)))
                                return onehand(hand[:],D+1)
                #"""
                rpar = 0
                for j in hand:
                    rpar += sum(j)
                if rpar > par:
                    par = rpar
                    print(par*100//(len(hand)**2 + 3*len(hand)))
                return hand
        else:
            if n < hand[p[0]][p[1]]:
                hand[p[0]][p[1]] = 0
                if p[1] == 1:
                    p[1] += 1
                    n -= 1
                else:
                    p = [p[0]+1,0]
            else:
                hand[p[0]][p[1]] += 1
                #"""
                #print(hand)
                if D < 500:
                    for i in hand:
                        if i[0] == 0 or i[0] == 2:
                            if i[1] <= i[2]:
                                rpar = 0
                                for j in hand:
                                    rpar += sum(j)
                                if rpar > par:
                                    par = rpar
                                    print(par*100//(len(hand)**2 + 3*len(hand)))
                                return onehand(hand[:],D+1)
                #"""
                rpar = 0
                for j in hand:
                    rpar += sum(j)
                if rpar > par:
                    par = rpar
                    print(par*100//(len(hand)**2 + 3*len(hand)))
                return hand

        if p == [len(hand),0]:
            return "end"

def doall(hand,log):#手順を一通り実行
    sign = ["+","-","×","÷"]
    value = []
    for i in range(len(log)):
        value.append(int2frac(log[i]))
        log[i] = str(log[i])
    
    for i in hand:
        keep = action(i[1:],sign[i[0]],value,log)
        value = keep[0]
        log = keep[1]
    return (value,log)

#"""
goal = input("goal number ")
goal = int2frac(int(goal))
nlist = input("can use numbers(Separated by spaces) ")
log = nlist.split(" ")
hand = []
for i in range(len(log)-1):
    hand.append([0,0,0])
result = []

while not(hand == "end"):
    keep = doall(hand,log[:])
    if keep[0][0] == goal:
        result.append(keep[1][0])
    hand = onehand(hand)

if result == []:
    print("nothing")
else:
    for i in result:
        print(i)
    print(str(len(result))+ " ways")
#"""
