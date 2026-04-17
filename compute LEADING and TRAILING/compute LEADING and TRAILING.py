# Program to compute LEADING and TRAILING

grammar = {
    "E": ["E+T", "T"],
    "T": ["T*F", "F"],
    "F": ["(E)", "id"]
}

leading = {}
trailing = {}

for non_terminal in grammar:
    leading[non_terminal] = set()
    trailing[non_terminal] = set()


# compute LEADING
changed = True
while changed:

    changed = False

    for nt in grammar:

        for production in grammar[nt]:

            first_symbol = production[0]

            # if terminal
            if not first_symbol.isupper():
                if first_symbol not in leading[nt]:
                    leading[nt].add(first_symbol)
                    changed = True

            else:
                for symbol in leading[first_symbol]:
                    if symbol not in leading[nt]:
                        leading[nt].add(symbol)
                        changed = True


# compute TRAILING
changed = True
while changed:

    changed = False

    for nt in grammar:

        for production in grammar[nt]:

            last_symbol = production[-1]

            # if terminal
            if not last_symbol.isupper():
                if last_symbol not in trailing[nt]:
                    trailing[nt].add(last_symbol)
                    changed = True

            else:
                for symbol in trailing[last_symbol]:
                    if symbol not in trailing[nt]:
                        trailing[nt].add(symbol)
                        changed = True


# display output
print("\nLEADING SET\n")

for nt in leading:
    print("LEADING(", nt, ") = ", leading[nt])

print("\nTRAILING SET\n")

for nt in trailing:
    print("TRAILING(", nt, ") = ", trailing[nt])