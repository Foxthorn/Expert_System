from string import strip
import sys


class Validate:
    __data = []
    __valid = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z', '+', '|', '=', '>', '<', '?', ' ', '!', '^', '(', ')']

    def __init__(self, filename):
        try:
            lists = []
            fd = open(filename, 'r')
            line = fd.readline()
            while line:
                lists.append(line)
                line = fd.readline()
            fd.close()
        except IOError:
            print 'Error: Cannot read file'
            sys.exit(1)
        for line in lists:
            text = strip(line.split('#', 1)[0])
            if not ((text == '\n') | (text == '')):
                for char in text:
                    if not (char in self.__valid):
                        print 'Error: Invalid Char in file'
                        sys.exit(1)
                self.__data.append(''.join(text.split()))

    def sort_lines(self, kb):
        query = self.get_queries()
        prio = []
        lines = []
        i = 0
        j = 0
        for char in query[0]:
            for c in char:
                if char == '?':
                    continue
                prio.append(char)
        while len(lines) != len(kb) and j <= len(prio):
            equals = kb[i].split('=>', 1)[1]
            if prio[j] in equals and kb[i] not in lines:
                lines.append(kb[i])
                letters = strip(kb[i].split('=', 1)[0])
                for char in letters:
                    if char.isalpha() and char not in prio:
                        prio.append(char)
                j += 1
                i = 0
            i += 1
            if i == len(kb):
                j += 1
                i = 0
        lines.reverse()
        return lines

    def get_kb(self):
        out = []
        for line in self.__data:
            if not ((line[0] == '=') | (line[0] == '?')):
                out.append(line)
        out = self.sort_lines(out)
        return out

    def get_facts(self):
        out = []
        for line in self.__data:
            if line[0] == '=':
                out.append(line)
        return out

    def get_queries(self):
        out = []
        for line in self.__data:
            if line[0] == '?':
                if len(line) < 2:
                    print 'Error: Please give a query'
                    sys.exit(1)
                out.append(line)
        if len(out) == 0:
            print 'Error: No Queries given'
            sys.exit(1)
        return out

    def get_dictionary(self):
        var_list = {}
        for line in self.__data:
            for char in line:
                if char.isalpha():
                    if char not in var_list:
                        var_list[char] = False
        return var_list
