from validate import *
from query import *
from brackets import *


def update_facts(f, v_list):
    no_i = 0
    for line in f:
        for char in line:
            if char == "!":
                no_i = 1
            if char.isalpha() and no_i == 0:
                v_list[char] = True
            if char.isalpha() and no_i == 1:
                v_list[char] = False
    return v_list


arg = len(sys.argv)
if arg == 1:
    print ('Usage: python main.py [filename]')
    sys.exit(1)
i = 1
while arg > i:
    change = True
    print "---------- "+sys.argv[i]+" ----------"
    val = Validate(sys.argv[i])
    kb = Validate.get_kb(val)
    facts = val.get_facts()
    q = Validate.get_queries(val)
    val_list = Validate.get_dictionary(val)
    val_list = update_facts(facts, val_list)
    solve = Solve(kb)
    while change is True:
        change = False
        val_list = solve.split_solve(val_list)
        if solve.change is True:
            change = True
    query = Query(val_list)
    if facts != [] and q != []:
        query.facts(facts)
        print "\n",
        query.query(q)
    else:
        print "No facts stated"
    i = i + 1
