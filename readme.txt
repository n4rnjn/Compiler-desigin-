PHASE 1 — LEXICAL ANALYSIS

File:
lexical.cpp

Purpose:
The lexical analyzer reads the source code and converts it into tokens such as keywords, identifiers, operators, numbers, and delimiters.

Example Input (input.c):

int a = 10;
float b = a + 20;

Output:

TOKENS GENERATED

<KEYWORD, int>
<IDENTIFIER, a>
<OPERATOR, =>
<NUMBER, 10>
<DELIMITER, ;>
<KEYWORD, float>
<IDENTIFIER, b>
<OPERATOR, =>
<IDENTIFIER, a>
<OPERATOR, +>
<NUMBER, 20>
<DELIMITER, ;>

Explanation:
The program scans the source file character by character and groups characters into meaningful tokens.

PHASE 2 — SYNTAX ANALYSIS

File:
syntax.cpp

Purpose:
The syntax analyzer checks whether the sequence of tokens follows valid grammar rules.

Example Input Expression:

a + 5 * b

Simulated Token Input:

<IDENTIFIER , a>
<OPERATOR , +>
<NUMBER , 5>
<OPERATOR , *>
<IDENTIFIER , b>

Output:

Parsing Successful: Syntax is correct

Example Invalid Input:

a + * b

Output:

Syntax Error in F()

Explanation:
The parser uses recursive descent parsing based on grammar rules.

Grammar Used:

E → T E'
E' → + T E' | ε
T → F T'
T' → * F T' | ε
F → (E) | id | number

PHASE 3 — SEMANTIC ANALYSIS

File:
semantic.cpp

Purpose:
The semantic analyzer ensures the program is meaningful by checking:

• Variable declaration
• Type compatibility
• Undeclared variables
• Duplicate declarations

Example Input:

Enter number of statements: 3

int a
a = 10
int b

Output:

Declared variable: a of type int
Assignment valid: a = 10
Declared variable: b of type int

Symbol Table

a : int
b : int

Example Error Case:

Input:

Enter number of statements: 1
a = 5

Output:

Semantic Error: Variable 'a' not declared

Explanation:
A symbol table stores variable names and their data types.

PHASE 4 — INTERMEDIATE CODE GENERATION

File:
intermediate.cpp

Purpose:
This phase converts expressions into Three Address Code (TAC).

Example Input:

Enter arithmetic expression:
a+b*c

Output:

Generated Three Address Code:

t1 = b * c
t2 = a + t1

Example Input:

(a+b)*(c+d)

Output:

t1 = a + b
t2 = c + d
t3 = t1 * t2

Explanation:
Temporary variables (t1, t2, t3) store intermediate results.

PHASE 5 — CODE OPTIMIZATION

File:
optimization.cpp

Purpose:
Optimization improves intermediate code efficiency without changing program behavior.

Techniques Used:

• Constant Folding
• Common Subexpression Elimination

Example Input:

Enter number of TAC instructions: 3

t1 = 2 + 3
t2 = a + b
t3 = a + b

Output:

Optimized Code:

t1 = 5
t2 = a + b
t3 = t2

Explanation:

2 + 3 is simplified to 5 (Constant Folding)
Repeated expression a + b is reused (Common Subexpression Elimination)

PHASE 6 — CODE GENERATION

File:
codegen.cpp

Purpose:
This phase converts optimized intermediate code into assembly-like instructions.

Example Input:

Enter number of TAC instructions: 2

t1 = b * c
t2 = a + t1

Output:

Generated Assembly Code:

LOAD b
MUL c
STORE t1

LOAD a
ADD t1
STORE t2