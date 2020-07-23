import pytest 
from Code import fact

def test_fact():
    assert fact.fact(9,4) == 11106
    assert fact.fact(2,5) == 24690