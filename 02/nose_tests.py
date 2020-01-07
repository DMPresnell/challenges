from nose.tools import *

from my_data import _load_words, LETTER_SCORES, DICTIONARY, POUCH
from my_game import _is_possible, _calculate_value, draw_hand, possible_words
from my_game import find_max, main

def data_tests():    
    # DICTINARY tests
    dictionary = _load_words()
    assert_equal(len(dictionary), 235886)
    assert_equal(dictionary[0], "a")
    assert_equal(dictionary[-1], "zyzzogeton")
    
    # LETTER_SCORES tests
    assert_equal(len(LETTER_SCORES.keys()), 26)
    assert_equal(sum(LETTER_SCORES.values()), 87)
    
    
def my_game_tests():
    # _is_possible() tests
    res1 = _is_possible("abcdefg", "bad")
    res2 = _is_possible("abcdefg", "23%")
    assert_equal(res1, True)
    assert_equal(res2, False)
    
    # _calculate_value() tests
    res1 = _calculate_value("apple")
    assert_equal(res1, 9)
    
    # draw_hand() tests
    res1 = draw_hand(7)
    res2 = draw_hand(0)
    assert_equal(len(res1), 7)
    assert_equal(len(res2), 0)
    
    # possible_words() tests
    res1 = possible_words("abcdefg")
    assert len(res1) > 1
    assert "bad" in res1
    
    # find_max() tests
    res1 = find_max(["spam", "eggs", "spam"])
    assert_equal(res1, [("spam", 8), ("spam", 8)])