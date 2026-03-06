#include <iostream>
#include <vector>
#include <map>
#include <sstream>

using namespace std;

struct TAC {
    string result;
    string arg1;
    string op;
    string arg2;
};

bool isNumber(string s) {
    for(char c : s)
        if(!isdigit(c))
            return false;
    return true;
}

int compute(int a, int b, string op) {
    if(op == "+") return a + b;
    if(op == "-") return a - b;
    if(op == "*") return a * b;
    if(op == "/") return a / b;
    return 0;
}

int main() {

    int n;
    cout << "Enter number of TAC instructions: ";
    cin >> n;
    cin.ignore();

    vector<TAC> code;
    map<string,string> expressionTable;

    cout << "\nEnter TAC instructions (example: t1 = a + b)\n";

    for(int i=0;i<n;i++){

        string line;
        getline(cin,line);

        stringstream ss(line);

        TAC t;
        string eq;

        ss >> t.result >> eq >> t.arg1 >> t.op >> t.arg2;

        code.push_back(t);
    }

    cout << "\nOptimized Code:\n";

    for(auto &t : code){

        if(isNumber(t.arg1) && isNumber(t.arg2)){

            int val = compute(stoi(t.arg1),stoi(t.arg2),t.op);

            cout << t.result << " = " << val << endl;
            continue;
        }

        string expr = t.arg1 + t.op + t.arg2;

        if(expressionTable.count(expr)){

            cout << t.result << " = " << expressionTable[expr] << endl;

        } else {

            expressionTable[expr] = t.result;

            cout << t.result << " = " << t.arg1 << " " << t.op << " " << t.arg2 << endl;
        }
    }

    return 0;
}