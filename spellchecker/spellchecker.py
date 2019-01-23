# coding=utf-8
import re
import collections
from itertools import product, imap

VERBOSE = True
vowels = set('aeiouy')
alphabet = set('abcdefghijklmnopqrstuvwxyz')



def words(text):
    #фильтруем текст на слова
    return re.findall('[a-z]+', text.lower())


def train(text, model=None):
    # создаем модель - для каждого слова в тексте считаем частоту
    model = collections.defaultdict(lambda: 0) if model is None else model
    for word in words(text):
        model[word] += 1
    return model


def train_from_files(file_list, model=None):
    # то же самое только из файлов
    for f in file_list:
        model = train(file(f).read(), model)
    return model



def numberofdupes(string, idx):
    # подсчитывает количество случаев когда одинаковые буквы идут подряд
    # "abccdefgh", 2  returns 1
    initial_idx = idx
    last = string[idx]
    while idx + 1 < len(string) and string[idx + 1] == last:
        idx += 1
    return idx - initial_idx


def hamming_distance(word1, word2):
    # подсчет расстояния хемминга
    if word1 == word2:
        return 0
    dist = sum(imap(str.__ne__, word1[:len(word2)], word2[:len(word1)]))
    dist = max([word2, word1]) if not dist else dist + abs(len(word2) - len(word1))
    return dist


def frequency(word, word_model):
    return word_model.get(word, 0)



def variants(word):
    # получить всевозможные варианты для каждого слова с учетом перестановок, удалений и т.д.
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [a + b[1:] for a, b in splits if b]
    transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]
    replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
    inserts = [a + c + b for a, b in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)


def double_variants(word):
    return set(s for w in variants(word) for s in variants(w))


def reductions(word):
    # возвращаем все возможные варианты для слова после удалений дупликатов
    word = list(word)
    # ['h','i', 'i', 'i'] становится ['h', ['i', 'ii', 'iii']]
    for idx, l in enumerate(word):
        n = numberofdupes(word, idx)
        # if letter appears more than once in a row
        if n:
            flat_dupes = [l * (r + 1) for r in xrange(n + 1)][:3]
            for _ in range(n):
                word.pop(idx + 1)
            word[idx] = flat_dupes

    for p in product(*word):
        yield ''.join(p)


def vowelswaps(word):
    # вовращает список вариантов слова если поменять местами гласные
    word = list(word)
    for idx, l in enumerate(word):
        if type(l) == list:
            pass
        elif l in vowels:
            word[idx] = list(vowels)

    for p in product(*word):
        yield ''.join(p)


def both(word):
    # посчитать все компинации редукций и перестановок гласных
    for reduction in reductions(word):
        for variant in vowelswaps(reduction):
            yield variant



def suggestions(word, real_words, short_circuit=True):
    word = word.lower()
    if short_circuit:
        return ({word} & real_words or  # caps     "inSIDE" => "inside"
                set(reductions(word)) & real_words or  # repeats  "jjoobbb" => "job"
                set(vowelswaps(word)) & real_words or  # vowels   "weke" => "wake"
                set(variants(word)) & real_words or  # other    "nonster" => "monster"
                set(both(word)) & real_words or  # both     "CUNsperrICY" => "conspiracy"
                set(double_variants(word)) & real_words or  # other    "nmnster" => "manster"
                {"NO SUGGESTION"})
    else:
        return ({word} & real_words or
                (set(reductions(word)) | set(vowelswaps(word)) | set(variants(word)) | set(both(word)) | set(
                    double_variants(word))) & real_words or
                {"NO SUGGESTION"})


def best(inputted_word, suggestions, word_model=None):

    # выбираем лучшее слово по расстояни. хеминга
    suggestions = list(suggestions)

    def comparehamm(one, two):
        score1 = hamming_distance(inputted_word, one)
        score2 = hamming_distance(inputted_word, two)
        return cmp(score1, score2)

    def comparefreq(one, two):
        score1 = frequency(one, word_model)
        score2 = frequency(two, word_model)
        return cmp(score2, score1)

    freq_sorted = sorted(suggestions, cmp=comparefreq)[10:]  # take the top 10
    hamming_sorted = sorted(suggestions, cmp=comparehamm)[10:]  # take the top 10


if __name__ == '__main__':
    word_model = train(file('/usr/share/dict/words').read())
    real_words = set(word_model)

    texts = [
        'sherlockholmes.txt',
        'lemmas.txt',
    ]
    word_model = train_from_files(texts, word_model)

    try:
        while True:
            word = str(raw_input('>'))

            possibilities = suggestions(word, real_words, short_circuit=False)
            short_circuit_result = suggestions(word, real_words, short_circuit=True)
            if VERBOSE:
                print [(x, word_model[x]) for x in possibilities]
                print best(word, possibilities, word_model)
                print '---'
            print [(x, word_model[x]) for x in short_circuit_result]
            if VERBOSE:
                print best(word, short_circuit_result, word_model)

    except (EOFError, KeyboardInterrupt):
        exit(0)
