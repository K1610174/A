import pytest 
#import file

def test_string_gen_data_type():
    assert string_gen.string_gen("words") == ""

def test_string_gen_five_chars():
    assert string_gen.string_gen(len("words"))==5

def test_string_gen_lowercase():
    assert string_gen.string_gen("words".islower())==True