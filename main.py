#!/usr/bin/env python

from itertools import product as prod
from itertools import groupby
from hashlib import sha256
from lib.keymap import Keymap

full_charset = ["""~`!@#$%^&*(124578Ttherisan'od"""]

charsets = ['!$@%1425', 'Tthere ', "isain't", 'no','data', 'here.', '$&%*^(475869.']


def char_combs(charset, n):
    x = []
    for charset in charsets:
        x.append(prod(chars, repeat=n) for chars in charset)
    return x


def switched_chars(s):
    possible_strings = []
    for i in range(len(s) - 1):
        possible_strings.append(s[:i] + s[i + 1] + s[i] + s[i + 2:])
    return possible_strings


def missed_chars(s):
    possible_strings = []
    for i in range(len(s) - 1):
        possible_strings.append(s[:i] + s[i + 1:])
    return possible_strings


def doubled_chars(s):
    possible_strings = []
    for i in range(len(s)):
        possible_strings.append(s[:i] + s[i] + s[i:])
    return possible_strings


def missed_space(s):
    return [s[:i] + s[i + 1:] for i in s if s[i] == ' ']


def switched_case(s):
    possible_strings = []
    for i in range(len(s)):
        if not s[i].isupper():
            possible_strings.append(s[:i] + s[i].upper() + s[i + 1:])
        else:
            possible_strings.append(s[:i] + s[i].upper() + s[i + 1:])
    return possible_strings


def caps_lock(s):
    for i in range(len(s)):
        if not s[i].isupper():
            s = s[:i] + s[i].upper() + s[i + 1:]
        else:
            s = s[:i] + s[i].lower() + s[i + 1:]
    return s


def wrong_chars(keymap, s):
    possible_strings = []
    for i in range(len(s)):
        if s[i] == ' ':
            possible_strings.append(s[:i] + s[i + 1:])
        else:
            neighbors = [char for char in keymap.get_neighbors(keymap, s[i]) if len(char) < 2]
            for n in range(len(neighbors)):
                possible_strings.append(s[:i] + neighbors[n] + s[i + 1:])
    return possible_strings


def main():
    test_string = '`echo This is the 1st 7357 57R1ng. | '
    switched = switched_chars(test_string)
    missed = missed_chars(test_string)
    typos = wrong_chars(keymap, test_string)
    for _ in switched:
        print(_)
    for _ in missed:
        print(_)
    for s_a in typos:
        print('"', s_a, '"')
        for s_c in missed_chars(s_a):
            print('"', s_c, '"')
            print(sha256(s_c.encode('utf-8')).hexdigest())
        for s_b in switched_chars(s_a):
            print('"' + s_b + '"')
            print(sha256(s_b.encode('utf-8')).hexdigest())


if __name__ == '__main__':
    test_string = '`echo This is the 1st 7357 57R1ng. | '
    keymap = Keymap()

    for i in range(len(test_string)):
        neighbors = keymap.get_neighbors(test_string[i])
        for n in range(len(neighbors)):
            s = test_string[:i] + neighbors[n] + test_string[i + 1:]
            print(s)
