#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct Token {
    string type;
    string value;
};

vector<Token> tokens;
int pos = 0;

Token currentToken() {
    if (pos < tokens.size())
        return tokens[pos];
    return {"EOF","EOF"};
}

void match(string expected) {
    if (currentToken().type == expected) {
        pos++;
    } else {
        cout << "Syntax Error: Expected " << expected 
             << " but found " << currentToken().type << endl;
        exit(1);
    }
}

void F();
void Tprime();
void T();
void Eprime();
void E();

void F() {
    if (currentToken().type == "IDENTIFIER" || currentToken().type == "NUMBER") {
        match(currentToken().type);
    }
    else if (currentToken().value == "(") {
        match("DELIMITER");
        E();
        if (currentToken().value == ")")
            match("DELIMITER");
        else {
            cout << "Syntax Error: Missing )" << endl;
            exit(1);
        }
    }
    else {
        cout << "Syntax Error in F()" << endl;
        exit(1);
    }
}

void Tprime() {
    if (currentToken().value == "*") {
        match("OPERATOR");
        F();
        Tprime();
    }
}

void T() {
    F();
    Tprime();
}

void Eprime() {
    if (currentToken().value == "+") {
        match("OPERATOR");
        T();
        Eprime();
    }
}

void E() {
    T();
    Eprime();
}

int main() {

    tokens = {
        {"IDENTIFIER","a"},
        {"OPERATOR","+"},
        {"NUMBER","5"},
        {"OPERATOR","*"},
        {"IDENTIFIER","b"}
    };

    E();

    if (pos == tokens.size())
        cout << "Parsing Successful: Syntax is correct\n";
    else
        cout << "Syntax Error\n";

    return 0;
}