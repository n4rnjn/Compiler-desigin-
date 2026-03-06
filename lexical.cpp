#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <cctype>
#include <unordered_set>

using namespace std;

// Token structure
struct Token {
    string type;
    string value;
};

// Keyword set
unordered_set<string> keywords = {
    "int","float","double","char","if","else","while","for","return","void","break","continue"
};

// Operators
unordered_set<string> operators = {
    "+","-","*","/","=","==","<",">","<=",">=","!="
};

// Delimiters
unordered_set<char> delimiters = {
    ';',',','(',')','{','}'
};

// Check identifier
bool isIdentifier(string str) {
    if (!isalpha(str[0]) && str[0] != '_')
        return false;

    for (char c : str) {
        if (!isalnum(c) && c != '_')
            return false;
    }
    return true;
}

// Check number
bool isNumber(string str) {
    for (char c : str) {
        if (!isdigit(c))
            return false;
    }
    return true;
}

vector<Token> tokenize(string code) {
    vector<Token> tokens;
    string buffer;

    for (size_t i = 0; i < code.length(); i++) {

        char c = code[i];

        // Skip whitespace
        if (isspace(c)) {
            if (!buffer.empty()) {
                if (keywords.count(buffer))
                    tokens.push_back({"KEYWORD", buffer});
                else if (isNumber(buffer))
                    tokens.push_back({"NUMBER", buffer});
                else if (isIdentifier(buffer))
                    tokens.push_back({"IDENTIFIER", buffer});
                buffer.clear();
            }
            continue;
        }

        // Operators
        if (string("+-*/=<>!").find(c) != string::npos) {

            if (!buffer.empty()) {
                if (keywords.count(buffer))
                    tokens.push_back({"KEYWORD", buffer});
                else if (isNumber(buffer))
                    tokens.push_back({"NUMBER", buffer});
                else if (isIdentifier(buffer))
                    tokens.push_back({"IDENTIFIER", buffer});
                buffer.clear();
            }

            string op(1,c);

            if (i+1 < code.length()) {
                string two = op + code[i+1];
                if (operators.count(two)) {
                    tokens.push_back({"OPERATOR", two});
                    i++;
                    continue;
                }
            }

            tokens.push_back({"OPERATOR", op});
            continue;
        }

        // Delimiters
        if (delimiters.count(c)) {

            if (!buffer.empty()) {
                if (keywords.count(buffer))
                    tokens.push_back({"KEYWORD", buffer});
                else if (isNumber(buffer))
                    tokens.push_back({"NUMBER", buffer});
                else if (isIdentifier(buffer))
                    tokens.push_back({"IDENTIFIER", buffer});
                buffer.clear();
            }

            tokens.push_back({"DELIMITER", string(1,c)});
            continue;
        }

        buffer += c;
    }

    if (!buffer.empty()) {
        if (keywords.count(buffer))
            tokens.push_back({"KEYWORD", buffer});
        else if (isNumber(buffer))
            tokens.push_back({"NUMBER", buffer});
        else if (isIdentifier(buffer))
            tokens.push_back({"IDENTIFIER", buffer});
    }

    return tokens;
}

int main() {

    ifstream file("input.c");

    if (!file.is_open()) {
        cout << "Error opening input file\n";
        return 1;
    }

    stringstream buffer;
    buffer << file.rdbuf();
    string code = buffer.str();

    vector<Token> tokens = tokenize(code);

    cout << "TOKENS GENERATED\n";
    cout << "-----------------\n";

    for (auto &t : tokens) {
        cout << "<" << t.type << ", " << t.value << ">" << endl;
    }

    return 0;
}