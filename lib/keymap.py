#!/usr/bin/env python


class Keymap:
    def __init__(self, name=None, matrices=None, indices=None, neighbors=None):
        self.name = name if name is not None else 'en_us'
        self.matrices = matrices if matrices is not None else {
            'lc': [
                ['`','1','2','3','4','5','6','7','8','9','0','-','=','BACK_SPACE'],
                ['TAB','q','w','e','r','t','y','u','i','o','p','[',']','\\','RETURN'],
                ['CAPS_LOCK','a','s','d','f','g','h','j','k','l',';','\''],
                ['LEFT_SHIFT','z','x','c','v','b','n','m',',','.','/','RIGHT_SHIFT'],
                [' ']
            ],
            'uc': [
                ['~','!','@','#','$','%','^','&','*','(',')','_','+','BACK_SPACE'],
                ['TAB','Q','W','E','R','T','Y','U','I','O','P','{','}','|','RETURN'],
                ['CAPS_LOCK', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"'],
                ['LEFT_SHIFT','Z','X','C','V','B','N','M','<','>','?','RIGHT_SHIFT'],
                [' ']
            ]
        }
        self.indices = {
            'lc': {},
            'uc': {}
        }

        for i, r in enumerate(self.matrices['lc']):
            for c in range(len(r)):
                self.indices['lc'][r[c]] = (i, c)
        for i, r in enumerate(self.matrices['uc']):
            for c in range(len(r)):
                self.indices['uc'][r[c]] = (i, c)

        self.neighbors = {}

        for key in self.matrices:
            for y, row in enumerate(self.matrices[key]):
                for x, char in enumerate(row):
                    self.neighbors[char] = []
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if y + i < 0 or x + j < 0 or (i == 0 and j == 0):
                                pass
                            else:
                                try:
                                    self.neighbors[char].append(self.matrices[key][y + i][x + j])
                                except IndexError:
                                    pass

    def get_case(self, char):
        case = None
        try:
            for index, row in enumerate(self.matrices['lc']):
                if char in row:
                    case = 'lc'
            if case is not None:
                return case
        finally:
            for index, row in enumerate(self.matrices['uc']):
                if char in row:
                    case = 'uc'
            return case

    def set_index(self, char):
        for index, row in enumerate(self.matrices['lc']):
            if char in row:
                self.indices['lc'][char] = (index, row.index(char))
            else:
                for index, row in enumerate(self.matrices['uc']):
                    if char in row:
                        self.indices['uc'][char] = (index, row.index(char))

    def set_indicies(self):
        print('set_indicies')
        for key in self.matrices:
            for row in self.matrices[key]:
                for char in row:
                    self.set_index(char)

    def get_index(self, char):
        try:
            index = self.indices['lc'][char]
        except KeyError:
            index = self.indices['uc'][char]
        return index

    def set_neighbors(self):
        for key in self.matrices:
            for y, row in enumerate(self.matrices[key]):
                for x, char in enumerate(row):
                    self.neighbors[char] = []
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if y + i < 0 or x + j < 0 or (i == 0 and j == 0):
                                pass
                            else:
                                try:
                                    self.neighbors[char].append(self.matrices[key][y + i][x + j])
                                except IndexError:
                                    pass

    def get_neighbors(self, char):
        return [i for i in self.neighbors[char] if len(i) < 2]


def main():
    test_string = '`echo This is the 1st 7357 57R1ng. | '
    keymap = Keymap()
    # keymap.set_indicies()
    # keymap.set_neighbors()

    for i in range(len(test_string)):
        neighbors = keymap.get_neighbors(test_string[i])
        for n in range(len(neighbors)):
            s = test_string[:i] + neighbors[n] + test_string[i + 1:]
            print(s)


if __name__ == '__main__':
    main()
