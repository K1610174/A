import pytest 
from Code import duplicates

def test_dupes():
    assert duplicates.dupes("hello world and practice makes perfect and hello world") == ("and hello makes perfect practice world")