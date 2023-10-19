# coding=utf-8

# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

import re
sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

count = {}
for sentence in sentences:
    sentence = re.sub("[^a-zA-Z]+$", '', sentence) 
    words = sentence.strip().lower().split(' ')
    for word in words:
        if word not in count:
            count[word] = 0
        count[word] += 1

count = dict(sorted(count.items(), key=lambda x: (-x[1], x[0])))
for i, x in enumerate(list(count.items())[:3]):
    place = str(i + 1) + '.'
    word = '"' + str(x[0]) + '"'
    count = x[1]
    print(place, word, '-', count)

# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2


# Good luck! You can write all the code in this file.
