#include <iostream>
#include <vector>
#include <string>
#include <stack>
using namespace std;

int main() {
	string line;
	cin >> line;

	vector<string> tokens;

	string t;
	for (int i = 0; i < line.size(); i++) {
		if (line[i] == '+' || line[i] == '-') {
			if (!t.empty()) {
				tokens.push_back(t);
				t.clear();
			}
			tokens.push_back(string(1, line[i]));
		}
		else {
			t += line[i];
		}
	}
	tokens.push_back(t);

	int total = 0, calc = 0;
	bool isMinus = false;
	for (auto it = tokens.begin(); it != tokens.end(); it++) {
		if (*it == "-") {
			if (!isMinus) {
				total += calc;
				calc = 0;
				isMinus = true;
			}
			else {
				total -= calc;
				calc = 0;
			}
		}
		else if (*it == "+") continue;
		else {
			if (isMinus)
				calc += stoi(*it);
			else
				total += stoi(*it);
		}
	}

	if (isMinus)
		total -= calc;

	cout << total << '\n';
}