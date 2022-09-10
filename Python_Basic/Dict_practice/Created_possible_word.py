"""This program take word from word_sample.exe then user need to input some alphabet
then the program will show possible word that can create."""


def read_file(filename):
    """Read sample.txt file and split to lines."""
    line = open(filename).read().splitlines()
    return line


def character_input():
    character_lst = []
    i = 1
    while len(character_lst) <= 5:
        char = input(f"Character {i} :")
        character_lst.append(char)
        i += 1
    return character_lst


def check_word(word):
    """Check all word."""
    checked_word = {}
    for i in word:
        checked_word[i] = 0
    return checked_word


def possible_word(all_word, char_lst):
    """Check that word can create by character in character list"""
    for word in all_word:
        char_in = 0
        for char in char_lst:
            if char in word:
                char_in += 1
        if char_in == len(word):
            checked_word[word] = 1
    return checked_word


def print_possible_word(checked_word):
    """Print possible word"""
    possible_word_lst = []
    for word in checked_word:
        if checked_word[word] == 1:
            possible_word_lst.append(word)
    if possible_word_lst is None:
        print(f"Character you in put can't create any word in word_smple.txt")
    print(f"Possible word can create is ")
    print(possible_word_lst)


if __name__ == "__main__":
    word_lst = read_file("word_sample.txt")
    characters = character_input()
    checked_word = check_word(word_lst)
    possible_word_check = possible_word(word_lst, characters)
    print_possible_word(possible_word_check)
