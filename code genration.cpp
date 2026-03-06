#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

struct TAC {
    string result;
    string arg1;
    string op;
    string arg2;
};

int main() {

    int n;

    cout << "Enter number of TAC instructions: ";
    cin >> n;
    cin.ignore();

    vector<TAC> code;

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

    cout << "\nGenerated Assembly Code:\n\n";

    for(auto &t : code){

        cout << "LOAD " << t.arg1 << endl;

        if(t.op == "+")
            cout << "ADD " << t.arg2 << endl;

        else if(t.op == "-")
            cout << "SUB " << t.arg2 << endl;

        else if(t.op == "*")
            cout << "MUL " << t.arg2 << endl;

        else if(t.op == "/")
            cout << "DIV " << t.arg2 << endl;

        cout << "STORE " << t.result << endl << endl;
    }

    return 0;
}