# LL(1) Parsing Table Construction

grammar = {
    'E': [['T', 'E1']],
    'E1': [['+', 'T', 'E1'], ['ε']],
    'T': [['F', 'T1']],
    'T1': [['*', 'F', 'T1'], ['ε']],
    'F': [['(', 'E', ')'], ['id']]
}

FIRST = {
    'E': {'(', 'id'},
    'E1': {'+', 'ε'},
    'T': {'(', 'id'},
    'T1': {'*', 'ε'},
    'F': {'(', 'id'}
}

FOLLOW = {
    'E': {')', '$'},
    'E1': {')', '$'},
    'T': {'+', ')', '$'},
    'T1': {'+', ')', '$'},
    'F': {'*', '+', ')', '$'}
}


# find terminals
terminals = set()

for rules in grammar.values():
    for rule in rules:
        for symbol in rule:
            if symbol not in grammar and symbol != 'ε':
                terminals.add(symbol)

terminals.add('$')


# create parsing table
table = {}

for non_terminal in grammar:
    table[non_terminal] = {}

    for rule in grammar[non_terminal]:

        first_set = set()

        if rule[0] == 'ε':
            first_set.add('ε')

        else:
            for symbol in rule:

                first_set.update(FIRST.get(symbol, {symbol}) - {'ε'})

                if 'ε' not in FIRST.get(symbol, {symbol}):
                    break
            else:
                first_set.add('ε')


        for terminal in first_set - {'ε'}:
            table[non_terminal][terminal] = rule


        if 'ε' in first_set:
            for terminal in FOLLOW[non_terminal]:
                table[non_terminal][terminal] = rule


# print parsing table
print("\nLL(1) PARSING TABLE\n")

print("{:8}".format(""), end="")

for t in terminals:
    print("{:12}".format(t), end="")

print()

for nt in grammar:

    print("{:8}".format(nt), end="")

    for t in terminals:

        if t in table[nt]:
            print("{:12}".format(nt + "->" + " ".join(table[nt][t])), end="")
        else:
            print("{:12}".format(" "), end="")

    print()