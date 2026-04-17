# Predictive Parsing (LL1 Parser)

# Grammar
grammar = {
    'E': [['T', 'E1']],
    'E1': [['+', 'T', 'E1'], ['ε']],
    'T': [['F', 'T1']],
    'T1': [['*', 'F', 'T1'], ['ε']],
    'F': [['(', 'E', ')'], ['id']]
}

# Parsing Table
table = {
    'E': {
        'id': ['T', 'E1'],
        '(': ['T', 'E1']
    },

    'E1': {
        '+': ['+', 'T', 'E1'],
        ')': ['ε'],
        '$': ['ε']
    },

    'T': {
        'id': ['F', 'T1'],
        '(': ['F', 'T1']
    },

    'T1': {
        '+': ['ε'],
        '*': ['*', 'F', 'T1'],
        ')': ['ε'],
        '$': ['ε']
    },

    'F': {
        'id': ['id'],
        '(': ['(', 'E', ')']
    }
}


# input string
input_string = "id + id * id"

# tokenize input
input_tokens = input_string.split()
input_tokens.append('$')

# stack initialization
stack = ['$','E']

print("\nSTACK\t\tINPUT\t\tACTION\n")

while len(stack) > 0:

    top = stack[-1]
    current_input = input_tokens[0]

    print(stack,"\t",input_tokens, end="\t")

    # if terminal matches
    if top == current_input:
        stack.pop()
        input_tokens.pop(0)
        print("match", current_input)

    # if epsilon
    elif top == 'ε':
        stack.pop()
        print("remove ε")

    # if non-terminal
    elif top in table:

        if current_input in table[top]:

            production = table[top][current_input]

            stack.pop()

            if production != ['ε']:
                for symbol in reversed(production):
                    stack.append(symbol)

            print(top,"->"," ".join(production))

        else:
            print("ERROR")
            break

    else:
        print("ERROR")
        break


# final result
if len(stack) == 0 and len(input_tokens) == 0:
    print("\nString Accepted")
else:
    print("\nString Rejected")