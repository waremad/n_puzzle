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

import math
import time

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

#smhDWMY
def timish(self):#秒時間をわかりやすく変換する
    if self < 60:
        keep = str(int(self//1))
        while len(keep) < 2:
            keep = "0" + keep
        return "00m." + keep + "s"
    ls = ["s","m","h","D","W","M","Y"]
    tls = [1,60,3600,86400,86400*7,86400*30,86400*365.25]
    n = 1
    while self > tls[n]:
        n += 1
    n -= 1
    keep = int(self//tls[n])
    keep = str(keep)
    while len(keep) < 2:
        keep = "0" + keep
    out = keep + ls[n] + "."
    keep = str(int((self%tls[n])//tls[n-1]))
    while len(keep) < 2:
        keep = "0" + keep
    out = out + keep + ls[n-1]
    return out


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

upar = 0
dpar = 0
par = 0
start = 0
now = 0
def onehand(hand=[],D=0):#手順listを１つ進める
    if hand == []:
        return "end"

    global upar
    global dpar
    global par
    global start

    n = len(hand) - 1

    upar += 1
    if dpar == 0:
        dpar = math.factorial(n+1) * math.factorial(n+2) * 4 ** (n+1)
    
    p = [0,0]
    do = True
    if p == [len(hand),0]:
            return "end"

    def printpar():
        global upar
        global dpar
        global par
        global start
        global now
        if upar*1000//dpar > par*10:
            par = (upar*1000//dpar)/10
            now = time.time() - start
            strpar = str(par)
            while len(strpar) < len("99.9"):
                strpar = "0" + strpar
            strpar = strpar + "%"
            print(strpar,"  passed:",timish(now),"  maybe:",timish(now*dpar/upar-now))


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
                                printpar()
                                return onehand(hand[:],D+1)
                #"""
                printpar()
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
                                printpar()
                                return onehand(hand[:],D+1)
                #"""
                printpar()
                return hand

        if p == [len(hand),0]:
            #print(upar,dpar)
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
start = time.time()
log = nlist.split(" ")
while log[0] == "":
    log.pop(0)
while log[-1] == "":
    log.pop(-1)
hand = []
for i in range(len(log)-1):
    hand.append([0,0,0])
result = []

while not(hand == "end"):
    keep = doall(hand,log[:])
    if keep[0][0] == goal:
        result.append(keep[1][0])
        hand = []
    hand = onehand(hand)

if result == []:
    print("nothing")
else:
    for i in result:
        print(i,"=",goal[:-2])
    print(str(len(result))+ " ways")
print("Tiem:" + timish(now))
#"""
#