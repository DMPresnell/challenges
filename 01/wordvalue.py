from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
<<<<<<< HEAD
    with open(DICTIONARY, "r") as open_file:
        words = [word.strip() for word in open_file.readlines()
                if word != ""]
    return words
=======
    with open(DICTIONARY) as f:
        return [word.strip() for word in f.read().split()]
>>>>>>> b14b0d46c4fdbbaaada6ce2e3ce099bd496cc0f2

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
<<<<<<< HEAD
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
=======
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()
    return max(words, key=calc_word_value)
>>>>>>> b14b0d46c4fdbbaaada6ce2e3ce099bd496cc0f2

if __name__ == "__main__":
    pass # run unittests to validate
