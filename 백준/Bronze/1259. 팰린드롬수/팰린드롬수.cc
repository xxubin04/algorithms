#include <iostream>
using namespace std;

int main() {
	string line = "";

	while (true) {
		cin >> line;

		if (line == "0") break;

		bool palindrome = true;
		int start = 0, end = line.length() - 1;
		while (start <= end) {
			if (line[start] != line[end]) {
				cout << "no\n";
				palindrome = false;
				break;
			}
			else {
				start++;
				end--;
			}
		}
		if (palindrome) cout << "yes\n";
	}
}