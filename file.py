class File_Setup:
    __operations = ['|', '+', '^', '=', '>', '!', '?']

    def __init__(self):
        self.lines = []
        self.facts = ''
        self.query = ''

    def check_file(self, line):
        for str in line:
            str = ''.join(str.split())
            for char in str:
                if char == "#":
                    break
                if char.isalpha() and char.islower():
                    return False
                elif char not in self.__operations:
                    if char.isalpha():
                        continue
                    return False
        return True

    def file_setup(self, lines):
        if self.check_file(lines) is False:
            return
        for str in lines:
            string = ''
            str = ''.join(str.split())
            for char in str:
                if char == '#':
                    break
                else:
                    string = string + char
            if string != '':
                self.lines.append(string)
        for entries in self.lines:
            if entries.startswith('='):
                self.facts = entries
            elif entries.startswith('?'):
                self.query = entries
        self.lines.remove(self.facts)
        self.lines.remove(self.query)
