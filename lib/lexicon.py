#!/usr/bin/python

"""
	Lexicon:
	A slightly less naive approach to combining elements of the alphabet.
"""

import itertools

##########################################################################


class EnAlphabet:
    def __init__(self, lc_alpha_string):
        self.lc_alpha_string = "abcdefghijklmnopqrstuvwxyz"
        self.lc_alpha_list = list(lc_alpha_string)
        self.lc_ascii_values = [ord(x) for x in self.lc_alpha_list]
        self.lc_ascii_to_alpha_dict = dict(
            zip(self.lc_ascii_values, self.lc_alpha_list))
        self.lc_alpha_to_ascii_dict = dict(
            zip(self.lc_alpha_list, self.lc_ascii_values))

        self.uc_alpha_string = self.lc_alpha_string.swapcase()
        self.uc_alpha_list = list(self.uc_alpha_string)
        self.uc_ascii_values = [ord(x) for x in self.uc_alpha_list]
        self.uc_ascii_to_alpha_dict = dict(
            zip(self.uc_ascii_values, self.uc_alpha_list))
        self.uc_alpha_to_ascii_dict = dict(
            zip(self.uc_alpha_list, self.uc_ascii_values))

        self.dec_digits_string = "0123456789"
        self.dec_digits_list = list(self.dec_digits_string)
        self.dec_ascii_values = [ord(x) for x in self.dec_digits_string]
        self.dec_ascii_to_alpha_dict = dict(
            zip(self.dec_ascii_values, self.decimal_digits_list))

        self.special_chars_string = """`~!@#$%^&*()-_=+[{]}\|;:'",<.>/? """
        self.special_chars_list = list(self.special_chars_string)

        self.uc_hex_digits_string = "0123456789ABCDEF"
        self.uc_hex_digits_list = list(self.uc.hex_digits_string)
        self.lc_hex_digits_string = self.uc_hex_digits_string.lower()
        self.lc_hex_digits_list = list(self.lc_hex_digits_string)

        self.all_alpha_string = self.lc_alpha_string + self.uc_alpha_string
        self.all_alpha_num_string = self.lc_alpha_string + \
            self.uc_alpha_string + self.dec_digits_string
        self.keyboard_chars_string = self.lc_alpha_string + self.uc_alpha_string + \
            self.dec_digits_string + self.special_chars_string

        self.lc_alpha_by_freq = "etaoinshrlducmwyfgpbvkjxqz"
        self.uc_alpha_by_freq = self.lc_alpha_by_freq.swapcase()

        self.common_bigrams_by_freq = []
        self.common_trigrams_by_freq = []

        return self

    def custom_charset(name, charset_string):
        self[name] = charset_string
        return self


class EnWordClasses:
    def __init__(self):
        self.adverbs = ''
        self.nouns = ''
        self.adjectives = ''
        self.verbs = ''
        self.conjunctions = ''
        self.verb_forms = ''
        self.irregular_verbs = ''
        self.suppletive_verbs = ''
        self.defective_verbs = ''
        self.auxiliary_verbs = ''
        self.intransitive_verbs = ''
        self.transitive_verbs = ''
        self.ergative_verbs = ''
        self.impersonal_verbs = ''
        self.phrasal_verbs = ''
        self.coordinating_conjunctions = ''
        self.subordinating_conjunctions = ''
        self.verb_suppletive_forms = ''
        self.verb_irregular_forms = ''
        self.verb_singular_forms = ''
        self.verb_second_person_forms = ''
        self.present_participles = ''
        self.past_participles = ''
        self.countable_nouns = ''
        self.proper_nouns = ''
        self.collective_nouns = ''
        self.adjective_forms = ''
        self.irregular_adjectives = ''
        self.uncomparable_adjectives = ''


class EnSentenceStructures:
    def __init__(self):
        pass

    def statements():
        pass


class EsAlphabet:
    def __init__(self):
        pass


class DeAlphabet:
    def __init__(self):
        pass

##########################################################################

languages = ['English', 'BasicEnglish', 'Sina', 'Bidoyoh', 'Abkhaz', 'Adyghe', 'Afrikaans', 'Albanian', 'American', 'Sign', 'Language', 'Arabic', 'Aragonese', 'Armenian', 'Aymara', 'Balinese', 'Basque', 'Betawi', 'Bosnian', 'Breton', 'Bulgarian', 'Cantonese', 'Catalan', 'Chickasaw', 'Chinese', 'Coptic', 'Cornish', 'Corsican', 'Crimean', 'Tatar', 'Croatian', 'Czech', 'Danish', 'Dutch', 'Esperanto', 'Estonian', 'Ewe', 'Fiji', 'Hindi', 'Filipino', 'Finnish', 'French', 'Galician', 'Georgian', 'German', 'Greek', 'Modern', 'Ancient', 'Greek', 'Greenlandic', 'Haitian', 'Creole', 'Hawaiian', 'Hebrew', 'Hindi', 'Hungarian', 'Icelandic', 'Indonesian', 'Inuktitut', 'Interlingua', 'Irish', 'Italian', 'Japanese', 'Kabardian', 'Kannada', 'Kashubian', 'Khmer', 'Kinyarwanda', 'Korean', 'Kurdish', 'Kurd', 'Ladin',
             'Latgalian', 'Latin', 'Lingala', 'Livonian', 'Lojban', 'Lower', 'Sorbian', 'Low', 'German', 'Macedonian', 'Malay', 'Malayalam', 'Mandarin', 'Manx', 'Maori', 'Mauritian', 'Creole', 'Min', 'Nan', 'Mongolian', 'Norwegian', 'Old', 'Armenian', 'Old', 'English', 'Old', 'French', 'Old', 'Norse', 'Old', 'Prussian', 'Oriya', 'Pangasinan', 'Papiamentu', 'Pashto', 'Persian', 'Pitjantjatjara', 'Polish', 'Portuguese', 'Proto', 'Slavic', 'Rapa', 'Nui', 'Romanian', 'Russian', 'Sanskrit', 'Scots', 'Scottish', 'Gaelic', 'Serbian', 'Serbo', 'Croatian', 'Slovak', 'Slovene', 'Spanish', 'Sinhalese', 'Swahili', 'Swedish', 'Tagalog', 'Tajik', 'Tamil', 'Tarantino', 'Telugu', 'Thai', 'Tok', 'Pisin', 'Turkish', 'Ukrainian', 'Upper', 'Sorbian', 'Urdu', 'Uzbek', 'Venetian', 'Vietnamese', 'Vilamovian', 'Welsh', 'Xhosa', 'Yiddish']


def bigrams(word):
    return [word[_:_ + 2] for _ in range(0, len(word) - 1)]


def trigrams(word):
    return [word[_:_ + 3] for _ in range(0, len(word) - 2)]


def n_grams(word, n):
    return [word[_:_ + n] for _ in range(0, len(word) - (n - 1))]

##########################################################################


def gematria_sum(word):
    char_set = [' '] + [chr(x) for x in range(97, 123)]
    word_value = sum([char_set.index(letter) for letter in list(word.lower())])
    return word_value


def gematria_product(word):
    char_set = [' '] + [chr(x) for x in range(97, 123)]
    word_value = 1
    for _ in [char_set.index(letter) for letter in list(word.lower())]:
        word_value *= _
    return word_value

##########################################################################


def hamming_distance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


def levenshtein(s1, s2):
    """Return the levenshtein distance for two sequences"""
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)
    previous_row = xrange(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            # j+1 instead of j since previous_row and current_row are one
            # character longer
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]


def LCS(X, Y):
    """
            Return the length of the longest common substring for two strings/sequences.
    """
    m = len(X)
    n = len(Y)
    # An (m+1) times (n+1) matrix
    C = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
            else:
                C[i][j] = max(C[i][j - 1], C[i - 1][j])
    return C


def longest_common_substring(s1, s2):
    m = [[0] * (1 + len(s2)) for i in xrange(1 + len(s1))]
    longest, x_longest = 0, 0
    for x in xrange(1, 1 + len(s1)):
        for y in xrange(1, 1 + len(s2)):
            if s1[x - 1] == s2[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]


def dice_coefficient(a, b):
    if not len(a) or not len(b):
        return 0.0
    """ quick case for true duplicates """
    if a == b:
        return 1.0
    """ if a != b, and a or b are single chars, then they can't possibly match """
    if len(a) == 1 or len(b) == 1:
        return 0.0
    """ use python list comprehension, preferred over list.append() """
    a_bigram_list = [a[i:i + 2] for i in range(len(a) - 1)]
    b_bigram_list = [b[i:i + 2] for i in range(len(b) - 1)]
    a_bigram_list.sort()
    b_bigram_list.sort()
    # assignments to save function calls
    lena = len(a_bigram_list)
    lenb = len(b_bigram_list)
    # initialize match counters
    matches = i = j = 0
    while (i < lena and j < lenb):
        if a_bigram_list[i] == b_bigram_list[j]:
            matches += 2
            i += 1
            j += 1
        elif a_bigram_list[i] < b_bigram_list[j]:
            i += 1
        else:
            j += 1
    score = float(matches) / float(lena + lenb)
    return score


def main():
    pass


if __name__ == '__main__':
    main()
