from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, "r") as open_file:
        words = [word.strip() for word in open_file.readlines()
                if word != ""]
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    values = [LETTER_SCORES[letter.upper()] for letter in word if
                letter.upper() in LETTER_SCORES.keys()]
    return sum(values)

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY.
    Returns the highest value word.  Returns a list of words if 
    there is a tie for highest value."""
    if words == None:
        words = load_words()
        
    word_value_list = [{"word": word, "value": calc_word_value(word)}
                   for word in words]
                   
    sorted_word_value_list = sorted(word_value_list,
        key= lambda word_score_dict: word_score_dict["value"])
        
    return sorted_word_value_list[-1]["word"]

if __name__ == "__main__":
    pass # run unittests to validate
