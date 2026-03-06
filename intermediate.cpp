#include <iostream>
#include <stack>
#include <vector>
#include <string>

using namespace std;

int tempCount = 1;

string newTemp() {
    return "t" + to_string(tempCount++);
}

int precedence(char op) {
    if (op == '*' || op == '/')
        return 2;
    if (op == '+' || op == '-')
        return 1;
    return 0;
}

vector<string> generateTAC(string expr) {

    stack<string> values;
    stack<char> ops;
    vector<string> code;

    for (int i = 0; i < expr.length(); i++) {

        char c = expr[i];

        if (c == ' ')
            continue;

        if (isalnum(c)) {
            values.push(string(1, c));
        }

        else if (c == '(') {
            ops.push(c);
        }

        else if (c == ')') {

            while (!ops.empty() && ops.top() != '(') {

                string val2 = values.top(); values.pop();
                string val1 = values.top(); values.pop();
                char op = ops.top(); ops.pop();

                string temp = newTemp();

                code.push_back(temp + " = " + val1 + " " + op + " " + val2);

                values.push(temp);
            }

            ops.pop();
        }

        else if (c == '+' || c == '-' || c == '*' || c == '/') {

            while (!ops.empty() && precedence(ops.top()) >= precedence(c)) {

                string val2 = values.top(); values.pop();
                string val1 = values.top(); values.pop();
                char op = ops.top(); ops.pop();

                string temp = newTemp();

                code.push_back(temp + " = " + val1 + " " + op + " " + val2);

                values.push(temp);
            }

            ops.push(c);
        }
    }

    while (!ops.empty()) {

        string val2 = values.top(); values.pop();
        string val1 = values.top(); values.pop();
        char op = ops.top(); ops.pop();

        string temp = newTemp();

        code.push_back(temp + " = " + val1 + " " + op + " " + val2);

        values.push(temp);
    }

    return code;
}

int main() {

    string expr;

    cout << "Enter arithmetic expression: ";
    getline(cin, expr);

    vector<string> tac = generateTAC(expr);

    cout << "\nGenerated Three Address Code:\n";

    for (string line : tac)
        cout << line << endl;

    return 0;
}