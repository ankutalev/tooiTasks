import csv
import collections
import json
import xml.etree.ElementTree as ET
from functools import cmp_to_key

max_length = 0
longest_word = " "
counter = collections.Counter()
bigrams_counter = collections.Counter()
avito_rows = []


def calculate_info(list_of_words, max_length, longest_word):
    i = 0
    while i < len(list_of_words) - 1:
        word_length = len(list_of_words[i])
        if word_length > 3:
            counter[list_of_words[i]] += 1
        if word_length > max_length:
            max_length = word_length
            longest_word = list_of_words[i]
        bigrams_counter[list_of_words[i] + " " + list_of_words[i + 1]] += 1
        i += 1


def print_info_and_cleanup(task_name):
    print_info(task_name)
    max_length = 0
    longest_word = ""
    counter.clear()
    bigrams_counter.clear()


def print_info(task_name):
    print("Most common in" + task_name, counter.most_common(20))
    print("Least common in " + task_name, counter.most_common()[:-20:-1])
    print("Longest word in " + task_name, longest_word)
    print("Most common bigram in " + task_name, bigrams_counter.most_common(1))
    print("All words in avito " + task_name, sum(counter.values()))
    print("Unique words in " + task_name + "\n", len(list(counter)))


def compare_adverts(a, b):
    return float(a[len(a) - 1]) - float(b[len(b) - 1])


with open('stage3_test.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    startCheck = 0
    for row in spamreader:
        if startCheck != 0:
            avito_rows.append(row)
            words = row[2].split(" ")
            calculate_info(words, max_length, longest_word)
        startCheck = 1
    print_info_and_cleanup(" avito:")

with open('RomeoAndJuliet.json') as f:
    data = json.load(f)
    for acts in data['acts']:
        for scenes in acts['scenes']:
            for actions in scenes['action']:
                for phrase in actions['says']:
                    calculate_info(phrase.split(" "), max_length, longest_word)
    print_info_and_cleanup("romeo and juliet: ")

tree = ET.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
for child in root.findall('text'):
    paragraphs = child.find('paragraphs')
    for paragraph in paragraphs:
        sentences = paragraph.findall('sentence')
        for sentence in sentences:
            calculate_info(sentence.find('source').text.split(" "), max_length, longest_word)
print_info_and_cleanup("xml: ")

avito_rows.sort(key=cmp_to_key(compare_adverts))
print("AVITO SORTED")
for row in avito_rows:
    print("Header: ", row[2], "Cost: ", row[len(row) - 1])
