#include <iostream>
using namespace std;

int tc;

int main() {
	cin >> tc;

	while (tc--) {
		string ox;
		cin >> ox;

		int score = 0, total_score = 0;

		for (char c : ox) {
			if (c == 'O') {
				score++;
				total_score += score;
			}
			else if (c == 'X') {
				score = 0;
			}
		}
		cout << total_score << '\n';
	}
}