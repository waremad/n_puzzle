from n_puzzle import *

def test_int2frac():
    assert int2frac("") == "0/1"
    assert int2frac(0) == "0/1"
    assert int2frac(1) == "1/1"
    assert int2frac(1729) == "1729/1"

def test_str2frac():
    assert str2frac("") == [0,1]
    assert str2frac("1/1") == [1,1]
    assert str2frac("2/5") == [2,5]
    assert str2frac("13/7") == [13,7]
    assert str2frac("-3/11") == [-3,11]

def test_redufrac():
    assert redufrac("") == "0/1"
    assert redufrac("1/1") == "1/1"
    assert redufrac("4/2") == "2/1"
    assert redufrac("57/3") == "19/1"
    assert redufrac("7/91") == "1/13"
    assert redufrac("-81/9") == "-9/1"
    assert redufrac("-57/-3") == "19/1"

def test_addfrac():
    assert addfrac("","") == "0/1"
    assert addfrac("1/1","1/1") == "2/1"
    assert addfrac("1/2","-1/3") == "1/6"
    assert addfrac("2/9","-4/5") == "-26/45"
    assert addfrac("81/9","-21/-3") == "16/1"
    assert addfrac("-5/3","7/9") == "-8/9"

def test_mulfrac():
    assert mulfrac("","") == "0/1"
    assert mulfrac("1/1","1/1") == "1/1"
    assert mulfrac("1/2","-1/3") == "-1/6"
    assert mulfrac("2/9","-4/5") == "-8/45"
    assert mulfrac("81/9","-21/-3") == "63/1"
    assert mulfrac("-5/3","7/9") == "-35/27"

def test_subfrac():
    assert subfrac("","") == "0/1"
    assert subfrac("1/1","1/1") == "0/1"
    assert subfrac("1/2","-1/3") == "5/6"
    assert subfrac("2/9","-4/5") == "46/45"
    assert subfrac("81/9","-21/-3") == "2/1"
    assert subfrac("-5/3","7/9") == "-22/9"

def test_divfrac():
    assert divfrac("","1/1") == "0/1"
    assert divfrac("1/1","1/1") == "1/1"
    assert divfrac("1/2","-1/3") == "-3/2"
    assert divfrac("2/9","-4/5") == "-5/18"
    assert divfrac("81/9","-21/-3") == "9/7"
    assert divfrac("-5/3","7/9") == "-15/7"


def test_timish():
    assert timish(0.5) == "00m.00s"
    assert timish(1) == "00m.01s"
    assert timish(59) == "00m.59s"
    assert timish(77) == "01m.17s"
    assert timish(3005) == "50m.05s"
    assert timish(3725) == "01h.02m"

def test_aaction():
    sign = ["+","-","×","÷"]
    ls = ["2/1","1/2","2/3","4/3","5/1"]
    log = ["2","(1 ÷ 2)","(((1 ÷ 2) - (1 ÷ 3)) × 4)","(2 - (2 ÷ 3))","(3 + 2)"]
    assert action([0,3],sign[0],ls[:],log[:]) == (["1/2","2/3","4/3","7/1"],[
        "(1 ÷ 2)","(((1 ÷ 2) - (1 ÷ 3)) × 4)","(2 - (2 ÷ 3))","(2 + (3 + 2))"])
    assert action([2,1],sign[1],ls[:],log[:]) == (["2/1","4/3","5/1","1/6"],[
        "2","(2 - (2 ÷ 3))","(3 + 2)","((((1 ÷ 2) - (1 ÷ 3)) × 4) - (1 ÷ 2))"])
    assert action([4,1],sign[2],ls[:],log[:]) == (["2/1","2/3","4/3","5/2"],[
        "2","(((1 ÷ 2) - (1 ÷ 3)) × 4)","(2 - (2 ÷ 3))","((3 + 2) × (1 ÷ 2))"])
    assert action([3,2],sign[3],ls[:],log[:]) == (["2/1","1/2","5/1","2/1"],[
        "2","(1 ÷ 2)","(3 + 2)","((2 - (2 ÷ 3)) ÷ (((1 ÷ 2) - (1 ÷ 3)) × 4))"])
    assert action([0,0],"-",["3/2","1/4"],["(3 ÷ 2)","((1 ÷ 2) × (1 ÷ (3 - 1)))"]) == (["5/4"],[
        "((3 ÷ 2) - ((1 ÷ 2) × (1 ÷ (3 - 1))))"])

def test_onehand():
    assert onehand([[0,0,0]]) == [[1,0,0]]
    assert onehand([[3,0,0]]) == [[0,1,0]]
    assert onehand([[3,1,0]]) == "end"
    assert onehand([[0,0,0],[0,0,0]]) == [[1,0,0],[1,0,0]]
    assert onehand([[3,0,0],[0,0,0]]) == [[1,0,0],[1,0,0]]
    assert onehand([[3,1,0],[0,0,0]]) == [[1,0,0],[1,0,0]]
    assert onehand([[3,2,0],[0,0,0]]) == [[1,0,0],[1,0,0]]
    assert onehand([[3,1,1],[0,0,0]]) == [[1,0,0],[1,0,0]]
    assert onehand([[3,2,1],[0,0,0]]) == [[1,0,0],[1,0,0]]
    assert onehand([[3,2,1],[2,0,0]]) == [[1,0,0],[3,0,0]]
    assert onehand([[3,2,1],[3,0,0]]) == [[1,0,0],[0,1,0]]
    assert onehand([[3,2,1],[3,1,0]]) == "end"

def test_doall():
    assert doall([[0,0,0]],[1,1]) == (["2/1"],["(1 + 1)"])
    assert doall([[1,1,2],[3,2,1],[2,1,0]],[2,3,5,7]) == (["-8/5"],["(((3 - 7) ÷ 5) × 2)"])

