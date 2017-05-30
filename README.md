# Typo

### Fuck up your input intelligently.

![alt text](https://raw.githubusercontent.com/gcgworld/typo/master/assets/img/typos_matrix.png)

*I only wrote this to recover a password for an
external harddrive I encrypted that I wrote down/typed wrong.*


### Usage:

```~# typo --options "Your phrase."```


### Options:

--switched-chars 'the, hte, teh...'
--missed-chars 'Input: The => Out: Th, he'
--doubled-chars 'In: the => Out: tthe, thhe, thee'
--missed-spaces 'In: The string => Out: Thestring'
--switched-case 'In: the => Out: the, The, tHe, thE'
--caps-locked 'In: The => Out: tHE'
--wrong-chars 'In: the => Out: 5he, 6he, rhe, yhe, fhe, ghe, hhe, .. etc.'
--product [number] 'Cross product of all possible n-length char-combs of chars in string'
-r --recursive 'Recursively incorporates other options.'


### The Keymap Class

1) The keyboard is represented as 2 matrices. (UPPER and lower case)
2) The neighboring keys of each key in the matrices are determined on instantiation. (defaults to 'en_us' mapping)

***Looking for a list of international keyboard layouts w/ keycodes to supplement for this***


### Vice Iteration.

*If you comp-sci college types have a name for this already, and there is an implementation in python, drop me a line at [gcgworld@protonmail.com](mailto:gcgworld@protonmail.com) and let me know what it's called. I'd sincerely appreciate it.*

with 2 threads:

```
0000 ---> ffff

0001 ---- ffff
0002 ---- fffe
0003 ---- fffd
  |        |
 ...      ...
  |        |
cfff ---- d000
```

with 4 threads:

```
0000 ---- 4000 ---- bfff ---- ffff
0001 ---- 4001 ---- bffe ---- fffe
0002 ---- 4002 ---- bffd ---- fffd
  |         |        |         |
 ...       ...      ...       ...
  |         |        |         |
3fff ---- 7fff ---- 8000 ---- c000
```

# GENERAL LIFE WARNING: Only encrypt your hard drives first thing in the morning,
# after the second cup of coffee, when you are awake enough to type,
# and record the passphrases correctly.
