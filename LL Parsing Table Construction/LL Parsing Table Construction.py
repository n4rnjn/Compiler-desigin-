# LL(1) Parsing Table Construction
# epsilon can be written as: ε

from collections import defaultdict

# ----------- INPUT GRAMMAR -----------
grammar = {
    "E": [["T", "E'"]],
    "E'": [["+", "T", "E'"], ["ε"]],
    "T": [["F", "T'"]],
    "T'": [["*", "F", "T'"], ["ε"]],
    "F": [["(", "E", ")"], ["id"]]
}

start_symbol = list(grammar.keys())[0]

# ----------- FIRST & FOLLOW STORAGE -----------
first = defaultdict(set)
follow = defaultdict(set)


# ----------- FIRST FUNCTION -----------
def find_first(symbol):

    if symbol not in grammar:
        return {symbol}

    result = set()

    for production in grammar[symbol]:

        if production[0] == "ε":
            result.add("ε")
            continue

        for sym in production:

            sym_first = find_first(sym)

            result.update(sym_first - {"ε"})

            if "ε" not in sym_first:
                break
        else:
            result.add("ε")

    return result


# ----------- FOLLOW FUNCTION -----------
def find_follow(symbol):

    if symbol == start_symbol:
        follow[symbol].add("$")

    for lhs in grammar:
        for production in grammar[lhs]:

            for i, sym in enumerate(production):

                if sym == symbol:

                    if i + 1 < len(production):

                        next_symbol = production[i+1]

                        first_next = find_first(next_symbol)

                        follow[symbol].update(first_next - {"ε"})

                        if "ε" in first_next:
                            follow[symbol].update(find_follow(lhs))

                    else:

                        if sym != lhs:
                            follow[symbol].update(find_follow(lhs))

    return follow[symbol]


# ----------- COMPUTE FIRST -----------
for nt in grammar:
    first[nt] = find_first(nt)


# ----------- COMPUTE FOLLOW -----------
for nt in grammar:
    follow[nt] = find_follow(nt)


# ----------- GET TERMINALS -----------
terminals = set()

for productions in grammar.values():
    for prod in productions:
        for symbol in prod:
            if symbol not in grammar and symbol != "ε":
                terminals.add(symbol)

terminals.add("$")


# ----------- LL(1) TABLE -----------
table = defaultdict(dict)

for non_terminal in grammar:

    for production in grammar[non_terminal]:

        first_prod = set()

        # compute FIRST of production
        if production[0] == "ε":
            first_prod.add("ε")
        else:
            for symbol in production:

                symbol_first = find_first(symbol)

                first_prod.update(symbol_first - {"ε"})

                if "ε" not in symbol_first:
                    break
            else:
                first_prod.add("ε")

        # fill table
        for terminal in first_prod - {"ε"}:
            table[non_terminal][terminal] = production

        # epsilon case
        if "ε" in first_prod:

            for terminal in follow[non_terminal]:
                table[non_terminal][terminal] = production


# ----------- PRINT FIRST -----------
print("\nFIRST SET")
for nt in grammar:
    print(f"FIRST({nt}) = {first[nt]}")


# ----------- PRINT FOLLOW -----------
print("\nFOLLOW SET")
for nt in grammar:
    print(f"FOLLOW({nt}) = {follow[nt]}")


# ----------- PRINT TABLE -----------
print("\nLL(1) PARSING TABLE\n")

print("{:10}".format(" "), end="")

for t in terminals:
    print("{:15}".format(t), end="")

print()

for nt in grammar:

    print("{:10}".format(nt), end="")

    for t in terminals:

        if t in table[nt]:
            prod = " ".join(table[nt][t])
            print("{:15}".format(f"{nt} -> {prod}"), end="")
        else:
            print("{:15}".format(" "), end="")

    print()