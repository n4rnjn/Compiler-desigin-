#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <sstream>

using namespace std;

set<int> epsilonClosure(set<int> states, map<int, vector<int>> &epsilon) {
    stack<int> s;
    for (int st : states) s.push(st);

    while (!s.empty()) {
        int state = s.top();
        s.pop();

        for (int nxt : epsilon[state]) {
            if (states.find(nxt) == states.end()) {
                states.insert(nxt);
                s.push(nxt);
            }
        }
    }

    return states;
}

set<int> moveSet(set<int> states, char symbol,
                 map<pair<int,char>, vector<int>> &transitions) {

    set<int> result;

    for (int st : states) {
        auto key = make_pair(st, symbol);

        if (transitions.find(key) != transitions.end()) {
            for (int nxt : transitions[key]) {
                result.insert(nxt);
            }
        }
    }

    return result;
}

string setToString(set<int> s) {
    stringstream ss;
    ss << "{";

    for (auto it = s.begin(); it != s.end(); it++) {
        ss << *it;
        if (next(it) != s.end()) ss << ",";
    }

    ss << "}";
    return ss.str();
}

int main() {

    int n;
    cout << "Number of NFA states: ";
    cin >> n;

    int t;
    cout << "Number of transitions: ";
    cin >> t;

    map<pair<int,char>, vector<int>> transitions;
    map<int, vector<int>> epsilon;

    cout << "Enter transitions (from symbol to)\n";
    cout << "Use e for epsilon\n";

    for(int i=0;i<t;i++){
        int from,to;
        char symbol;

        cin >> from >> symbol >> to;

        if(symbol=='e')
            epsilon[from].push_back(to);
        else
            transitions[{from,symbol}].push_back(to);
    }

    int start;
    cout << "Start state: ";
    cin >> start;

    int f;
    cout << "Number of final states: ";
    cin >> f;

    set<int> finalStates;

    for(int i=0;i<f;i++){
        int x;
        cin >> x;
        finalStates.insert(x);
    }

    set<char> alphabet;

    for(auto &t : transitions)
        alphabet.insert(t.first.second);

    queue<set<int>> q;
    map<set<int>, bool> visited;

    set<int> startSet;
    startSet.insert(start);

    startSet = epsilonClosure(startSet, epsilon);

    q.push(startSet);
    visited[startSet] = true;

    map<pair<string,char>, string> dfa;

    cout << "\nDFA Construction:\n";

    while(!q.empty()) {

        set<int> current = q.front();
        q.pop();

        for(char symbol : alphabet) {

            set<int> move = moveSet(current, symbol, transitions);

            move = epsilonClosure(move, epsilon);

            if(move.empty()) continue;

            if(!visited[move]) {
                visited[move] = true;
                q.push(move);
            }

            dfa[{setToString(current),symbol}] = setToString(move);
        }
    }

    cout << "\nDFA Transition Table\n";

    for(auto &d : dfa) {

        cout << d.first.first
             << " -- " << d.first.second
             << " --> "
             << d.second << endl;
    }

    cout << "\nFinal DFA States:\n";

    for(auto &state : visited) {

        for(int f : finalStates) {

            if(state.first.count(f)) {
                cout << setToString(state.first) << endl;
                break;
            }
        }
    }

    return 0;
}