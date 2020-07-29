import pytest
from Code import amsterdam

def test_count():
    assert amsterdam.find_between("Am I in Amsterdam") == 1
    
def test_noAm():
    assert amsterdam.find_between("This is just a sentence") == 0