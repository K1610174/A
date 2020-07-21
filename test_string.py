import pytest 
import string_gen

def test_string_gen_data_type():
    assert isinstance(string_gen.string_gen(), str) == True

def test_string_gen_five_chars():
    assert len(string_gen.string_gen())==5

def test_string_gen_lowercase():
    for _ in range(20):
        assert string_gen.string_gen().islower()== True
