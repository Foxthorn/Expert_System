from file import *
from chaining import *
import sys

if len(sys.argv) > 2:
    print "To many arguments"
elif len(sys.argv) == 1:
    print "To little arguments"
else:
    fd = open(sys.argv[1])
    lines = fd.readlines()
    file = File_Setup()
    list = Chain()
    letters = Chain()
    file.file_setup(lines)
    for str in file.lines:
        list.add(str)
        for char in str:
            if char.isalpha() and letters.find(char) is False:
                letters.add(char)
    for char in file.facts:
        letters.set_true(char)
    letters.display_bool()
