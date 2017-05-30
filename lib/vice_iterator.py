#!/usr/bin/env python


from itertools import product as prod


def reverse_charset(charset):
    rev_charset = list(charset)
    rev_charset.reverse()
    rev_charset = ''.join(rev_charset)
    return rev_charset


def intersections(charset, n_chars, n_threads):
    # n_threads <= len(charset)
    total_iterations = len(charset) ** n_chars
    # if n_threads == 2:
    #     if len(charset) % 2 == 0:
    #         intersection = (len(charset) ** 2) / 2
    #     else:
    #         intersection = (len(charset) ** 2) + 1
    print('Total iterations:', total_iterations)


def vice(charset, n_chars, n_threads=int):
    rev_charset = reverse_charset(charset)
    charsets = [charset[i:] + charset[:i] for i in range(0, len(charset), int(len(charset)/n_threads))]
    rev_charsets = [rev_charset[i:] + rev_charset[:i] for i in range(0, len(rev_charset), int(len(rev_charset)/n_threads))]
    # charsets = charsets + rev_charsets
    # gens = [prod(charset, n_chars) for c_set in charsets]
    gens = [prod(charset, repeat=n_chars), prod(rev_charset, repeat=n_chars)]
    return gens


def main():
    charset = "012"
    gens = vice(charset, 3, 2)

    iterations = 0
    while True:
        if iterations == int((len(charset) ** 3) / 2):
            break
        else:
            print(iterations)
            for i in range(len(gens)):
                # print(i)
                print(next(gens[i]))
            iterations += 1

        # print('#' * 80)


if __name__ == '__main__':
    main()
