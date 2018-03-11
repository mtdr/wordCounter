import pymorphy2
import itertools


def norm(x):
    morph = pymorphy2.MorphAnalyzer()
    p = morph.parse(x)[0]
    return p.normal_form


path = "src.txt"
inputFile = open(path, "r", encoding='utf8')
lines = inputFile.read().splitlines()
wordsByLines = []
print(lines)
for line in lines:
    wordsByLines.append(line.split(' '))

words = []
for wordArr in wordsByLines:
    words += wordArr

print("Исходный массив")
print(words)

norm_word = []
for un_word in words:
    norm_word.append(norm(un_word))

print("Нормализованный массив")
print(norm_word)

my_dict = dict((x, norm_word.count(x)/len(words)) for x in set(norm_word))
print(my_dict)
