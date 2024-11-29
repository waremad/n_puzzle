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