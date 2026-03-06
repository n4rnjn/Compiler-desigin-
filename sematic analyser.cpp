#include <iostream>
#include <unordered_map>
#include <sstream>
#include <vector>

using namespace std;

// Symbol table
unordered_map<string, string> symbolTable;

// Split input line into tokens
vector<string> tokenize(string line) {
    vector<string> tokens;
    string token;
    stringstream ss(line);

    while (ss >> token) {
        tokens.push_back(token);
    }

    return tokens;
}

// Check if variable declared
bool isDeclared(string var) {
    return symbolTable.find(var) != symbolTable.end();
}

// Handle declaration
void handleDeclaration(vector<string> tokens) {

    string type = tokens[0];
    string var = tokens[1];

    if (symbolTable.find(var) != symbolTable.end()) {
        cout << "Semantic Error: Variable '" << var << "' already declared\n";
        return;
    }

    symbolTable[var] = type;

    cout << "Declared variable: " << var << " of type " << type << endl;
}

// Handle assignment
void handleAssignment(vector<string> tokens) {

    string var = tokens[0];

    if (!isDeclared(var)) {
        cout << "Semantic Error: Variable '" << var << "' not declared\n";
        return;
    }

    string type = symbolTable[var];
    string value = tokens[2];

    if (type == "int") {
        for (char c : value) {
            if (!isdigit(c)) {
                cout << "Type Error: Cannot assign non-int to int variable '" 
                     << var << "'\n";
                return;
            }
        }
    }

    cout << "Assignment valid: " << var << " = " << value << endl;
}

int main() {

    cout << "Enter number of statements: ";
    int n;
    cin >> n;
    cin.ignore();

    for (int i = 0; i < n; i++) {

        cout << "\nEnter statement: ";

        string line;
        getline(cin, line);

        vector<string> tokens = tokenize(line);

        if (tokens.size() == 2) {
            handleDeclaration(tokens);
        }
        else if (tokens.size() >= 3 && tokens[1] == "=") {
            handleAssignment(tokens);
        }
        else {
            cout << "Invalid statement format\n";
        }
    }

    cout << "\nSymbol Table\n";
    cout << "-----------------\n";

    for (auto &entry : symbolTable) {
        cout << entry.first << " : " << entry.second << endl;
    }

    return 0;
}