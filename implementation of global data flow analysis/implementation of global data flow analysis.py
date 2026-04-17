# Global Data Flow Analysis (Reaching Definitions)

# basic blocks
blocks = {
    "B1": ["a = 5", "b = 6"],
    "B2": ["a = b + 1"],
    "B3": ["c = a + b"]
}

# control flow graph (CFG)
# which block leads to which
cfg = {
    "B1": ["B2"],
    "B2": ["B3"],
    "B3": []
}

# GEN and KILL sets
GEN = {}
KILL = {}

# find definitions
definitions = {}

for block in blocks:
    GEN[block] = set()
    KILL[block] = set()

for block in blocks:

    for stmt in blocks[block]:

        var = stmt.split("=")[0].strip()

        definition = var + "_" + block

        GEN[block].add(definition)

        if var not in definitions:
            definitions[var] = []

        definitions[var].append(definition)


# compute KILL
for block in blocks:

    for d in GEN[block]:

        var = d.split("_")[0]

        for other_def in definitions[var]:

            if other_def != d:
                KILL[block].add(other_def)


# initialize IN and OUT
IN = {}
OUT = {}

for block in blocks:
    IN[block] = set()
    OUT[block] = set()


# iterative algorithm
changed = True

while changed:

    changed = False

    for block in blocks:

        # IN = union of predecessors OUT
        new_in = set()

        for pred in cfg:

            if block in cfg[pred]:
                new_in = new_in.union(OUT[pred])

        # OUT = GEN ∪ (IN - KILL)
        new_out = GEN[block].union(new_in - KILL[block])

        if new_in != IN[block] or new_out != OUT[block]:
            IN[block] = new_in
            OUT[block] = new_out
            changed = True


# display result
print("\nGEN sets")
for b in GEN:
    print(b, ":", GEN[b])

print("\nKILL sets")
for b in KILL:
    print(b, ":", KILL[b])

print("\nIN sets")
for b in IN:
    print(b, ":", IN[b])

print("\nOUT sets")
for b in OUT:
    print(b, ":", OUT[b])
    