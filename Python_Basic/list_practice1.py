"""This list practice program will read quote in sample.txt
and have function to display length of string,
Look for string word inside string text,
Count a number of character that user use inside string text
"""


def read_file(filename):
    """Read sample.txt file and split to lines."""
    line = open(filename).read().splitlines()
    return line


def find_length(sentences):
    """Find length for all quote in sample.txt ."""
    for i in range(len(sentences)):
        print(f"{len(sentences[i])} : {sentences[i]}")


def find_word(sentences, word):
    """Can check that word is in witch sentence in sample.txt and tell the index"""
    count_word = 0
    match_index = []
    for i in range(len(sentences)):
        if word.lower() == sentences[i:i + len(word)].lower():
            count_word = 1
            match_index.append(i)
    if count_word > 0:
        return True, match_index
    else:
        return False, match_index


def operate(sentence, choice_select):
    if choice_select == 1:
        print(find_length(sentence))
    elif choice_select == 2:
        word = input("Enter a word: ")
        for text in sentence:
            check, list_index = find_word(text, word)
            if check:
                print(f"{list_index} : {text}")
            else:
                print(f" : {text}")


# Main
filename = "sample.txt"
lines = read_file(filename)
print(lines)  # Uncomment this line to see what lines look like
print('1. Find length')
print('2. Find word')
choice = int(input('Enter choice: '))
operate(lines, choice)

