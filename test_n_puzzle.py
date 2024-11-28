from n_puzzle import *

def test_int2frac():
    assert int2frac() == ""
    assert int2frac(0) == "0/1"
    assert int2frac(1) == "1/1"
    assert int2frac(1729) == "1729/1"