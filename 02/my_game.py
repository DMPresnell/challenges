from collections import Counter
from random import choices

from my_data import POUCH, DICTIONARY, LETTER_SCORES

char_str = POUCH

def _is_possible(hand, word):
    # Used in possible_words().
    # check if the passed "word" can be spelled given the characters 
    # in "hand".
    hand_c = Counter(hand)
    word_c = Counter(word)
    for char, count in word_c.items():
        try:
            if hand_c[char] < count:
                return False
        except KeyError:
            return False
    return True

def _calculate_value(word):
    # Used in find_max().
    # Calculate the value of passed string using LETTER_SCORES and return it.
    return sum([LETTER_SCORES[char] for char in word if char.isalpha()])

def draw_hand(amount):
    # pick 7 random characters from "char_str" and return them as a list.
    return choices(char_str, k=amount)
    
def possible_words(hand):
    # return a list of all words that can be made with "hand".
    return [word for word in DICTIONARY if _is_possible(hand, word)]
    
def find_max(words):
    # Find the words from "words" that have the greatest value.
    # Return a list of tuples: [(word, value),...].
    words_value = [(word, _calculate_value(word)) for word in words]
    words_value.sort(key= lambda tuple: tuple[1])
    max_words = [words_value.pop()]
    while words_value[-1][1] == max_words[0][1]:
        max_words.append(words_value.pop())
    return max_words

def main():
    hand = draw_hand(7)
    poss_words = possible_words(hand)
    max_words = find_max(poss_words)
    
    print("")
    print("Your letters are:", end="")
    for letter in hand:
        print(" |" + letter.upper() + "|", end="")

    print("\n")
    print("The highest value word(s) you can make are:  ")
    for tuple in max_words:
        print(tuple[0])
    
    print("")
    print(f"This will get you {max_words[0][1]} points.")
    
if __name__ == "__main__":
    
    main()