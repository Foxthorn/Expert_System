from string import strip


class Solve:
    __data = []

    def __init__(self, kb):
        self.op = ['+', '|', '^', '(', ')', '=', '>']
        self.change = False
        self.exclude = []
        for line in kb:
            self.__data.append(line)

    @staticmethod
    def solve(equat):
        num = 0
        if '|' in equat:
            if 'T' in equat:
                return True
        if '+' in equat:
            for char in equat:
                if char == 'T':
                    num += 1
            if num == 2:
                return True
            else:
                return False
        if '^' in equat:
            for char in equat:
                if char == 'T':
                    num += 1
            if num == 1:
                return True
            else:
                return False
        if 'T' in equat:
            return True
        elif 'F' in equat:
            return False

    def solve_loop(self, split):
        done = False
        while done is False:
            i = 0
            equat = ''
            if '(' in split:
                while '(' in split:
                    while split[i] != '(' and i < len(split):
                        i += 1
                    split[i] = '#'
                    i += 1
                    while i < len(split) and split[i] != ')':
                        equat = equat + split[i]
                        split[i] = '#'
                        i += 1
                    split[i] = '#'
            elif '+' in split:
                while i < len(split):
                    if split[i] == '+':
                        equat = equat + split[i - 1]
                        equat = equat + split[i]
                        equat = equat + split[i + 1]
                        split[i - 1] = '#'
                        split[i] = '#'
                        split[i + 1] = '#'
                    i += 1
            else:
                num_char = 0
                while i < len(split) and num_char < 3:
                    if split[i] != '#':
                        equat = equat + split[i]
                        split[i] = '#'
                        num_char += 1
                    i += 1
            if i == len(split):
                i -= 1
            if self.solve(equat) is True:
                split[i] = 'T'
            else:
                split[i] = 'F'
            num_hash = 0
            for char in split:
                if char == '#':
                    num_hash += 1
            if num_hash == len(split) - 1:
                done = True
        return split[len(split) - 1]

    @staticmethod
    def convert_to_bool(line, varlist):
        i = 0
        num_var = 0
        split = []
        while i < len(line):
            char = line[i]
            if char.isalpha() and line[i - 1] == '!' and varlist[char] is True:
                split.append('F')
                i += 1
                num_var += 1
            elif char.isalpha() and line[i - 1] == '!' and varlist[char] is False:
                split.append('T')
                i += 1
                num_var += 1
            elif char.isalpha() and varlist[char] is True:
                split.append('T')
                i += 1
                num_var += 1
            elif char.isalpha() and varlist[char] is False:
                split.append('F')
                i += 1
                num_var += 1
            else:
                if char != '!':
                    split.append(char)
                i += 1
        return split

    def set_end_bool(self, end, split):
        i = 0
        while i < len(end):
            if end[i] in self.op:
                i += 1
                continue
            if split == 'T':
                end[i] = 'T'
            elif split == 'F':
                end[i] = 'F'
            i += 1
        return end

    def split_solve(self, varlist):
        self.change = False
        for line in self.__data:
            rule = line
            end = line.split('=>', 1)[1]
            line = strip(line.split('=', 1)[0])
            split = self.convert_to_bool(line, varlist)
            end = self.convert_to_bool(end, varlist)
            split = self.solve_loop(split)
            end = self.set_end_bool(end, split)
            i = 0
            end_set = rule.split('=>', 1)[1]
            while i < len(end_set):
                if end_set[i] in self.op:
                    i += 1
                    continue
                if end[i] == 'T':
                    if varlist[end_set[i]] is not True and end_set[i] not in self.exclude:
                        self.change = True
                    varlist[end_set[i]] = True
                    self.exclude.append(end_set[i])
                elif end[i] == 'F' and end_set[i] not in self.exclude:
                    if varlist[end_set[i]] is not False:
                        self.change = True
                    varlist[end_set[i]] = False
                    self.exclude.append(end_set[i])
                i += 1
        return varlist
