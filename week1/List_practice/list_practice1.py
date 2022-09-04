"""This list practice program will read quote in sample.txt
and have function to display length of string,
Look for string word inside string text,
Count a number of character that user use inside string text
"""


def read_file(filename):
    line = open(filename).read().splitlines()
    return line


def find_length(sentences):
    for i in range(len(sentences)):
        print(f"{len(sentences[i])} : {sentences[i]}")

def find_word(word):
    pass



s = read_file("sample.txt")
find_length(s)
