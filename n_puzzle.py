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
    if self == "" or self[0] == "0" or self[:2] == "-0":
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

