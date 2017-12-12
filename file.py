class File_Setup:
    def __init__(self):
        self.lines = []
        self.facts = ''
        self.query = ''

    def file_setup(self, lines):
        for str in lines:
            string = ''
            str = ''.join(str.split())
            for char in str:
                if char == '#' or char == '\n':
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
