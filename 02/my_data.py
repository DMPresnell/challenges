POUCH = ("aaaaaaaaabbccddddeeeeeeeeeeeeffgggghhiiiiiiiiijkllll"
        "mmnnnnnnooooooooppqrrrrrrssssttttttuuuuvvwwxyyz")
        
def _load_words():
    with open("dictionary.txt") as f:
        f_read = f.read()
    return [word.lower() for word in f_read.splitlines()]

DICTIONARY = _load_words()

LETTER_SCORES = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2,
    "h": 4, "i": 1, "j": 8, "k": 5, "l": 1, "m": 3, "n": 1, "o": 1, "p": 3,
    "q": 10, "r": 1, "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8, "y": 4,
    "z": 10}