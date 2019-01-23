from itertools import product
import random

vowels = {"a","e","i","o","u","y"}

def get_inflations(word):
    word = list(word)
    for idx, l in enumerate(word):
        if random.random() * 100 > 60:
            word[idx] = word[idx]*int(random.random()*10)
    return word

def get_vowelswaps(word):
    word = list(word)
    for idx, l in enumerate(word):
        if type(l) == list:
            pass
        elif l in vowels:
            word[idx] = list(vowels)
        
    return word

def flatten(options):
    a = set()
    for p in product(*options):
        a.add(''.join(p))
    return a

def misspell(word):

    return random.choice(list(flatten(get_vowelswaps(word)) | flatten(get_inflations(word))))

if __name__ == "__main__":

    words = ["fishy", "monster", "apple", "saint", "potato", "moth"]
    for word in words:
        print(misspell(word))
