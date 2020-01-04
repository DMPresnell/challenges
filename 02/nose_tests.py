from nose.tools import *

from my_data import _load_words, LETTER_SCORES

def data_tests():    
    # DICTINARY tests
    DICTIONARY = _load_words()
    assert_equal(len(DICTIONARY), 235886)
    assert_equal(DICTIONARY[0], "a")
    assert_equal(DICTIONARY[-1], "zyzzogeton")
    
    # LETTER_SCORES tests
    assert_equal(len(LETTER_SCORES.keys()), 26)
    assert_equal(sum(LETTER_SCORES.values()), 87)