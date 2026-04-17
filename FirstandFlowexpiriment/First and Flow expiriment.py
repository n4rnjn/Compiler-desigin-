# FIRST and FOLLOW in Compiler Design
# Supports epsilon as: ε or e or #

from collections import defaultdict

# ---------- INPUT GRAMMAR ----------
# Example grammar:
# E -> T E'
# E' -> + T E' | ε
# T -> F T'
# T' -> * F T' | ε
# F -> ( E ) | id

grammar = {
    "E": [["T", "E'"]],
    "E'": [["+", "T", "E'"], ["ε"]],
    "T": [["F", "T'"]],
    "T'": [["*", "F", "T'"], ["ε"]],
    "F": [["(", "E", ")"], ["id"]]
}

# ---------- GLOBAL VARIABLES ----------
first = defaultdict(set)
follow = defaultdict(set)
start_symbol = list(grammar.keys())[0]


# ---------- FIRST FUNCTION ----------
def find_first(symbol):
    
    # if terminal
    if symbol not in grammar:
        return {symbol}
    
    result = set()

    for production in grammar[symbol]:

        # epsilon production
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


# ---------- FOLLOW FUNCTION ----------
def find_follow(symbol):

    if symbol == start_symbol:
        follow[symbol].add("$")

    for lhs in grammar:
        for production in grammar[lhs]:

            for i, sym in enumerate(production):

                if sym == symbol:

                    # if not last symbol
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


# ---------- COMPUTE FIRST ----------
for non_terminal in grammar:
    first[non_terminal] = find_first(non_terminal)


# ---------- COMPUTE FOLLOW ----------
for non_terminal in grammar:
    follow[non_terminal] = find_follow(non_terminal)


# ---------- OUTPUT ----------
print("\nFIRST SET")
for nt in grammar:
    print(f"FIRST({nt}) = {first[nt]}")

print("\nFOLLOW SET")
for nt in grammar:
    print(f"FOLLOW({nt}) = {follow[nt]}")