#include <bits/stdc++.h>
using namespace std;

int tc;

int main() {
	cin >> tc;
	cin.ignore();

	while (tc--) {
		int tcNum;
		cin >> tcNum;
		cin.ignore();

		map<int, int> scoreCount;
		string line;
		getline(cin, line);
		stringstream ss(line);

		int num;
		int maxFreq = 0, mostFreqScore = 0;
		while (ss >> num)
			scoreCount[num]++;

		for (auto& s : scoreCount) {
			int score = s.first, freq = s.second;

			if (freq >= maxFreq || (freq == maxFreq && score > mostFreqScore))
				maxFreq = freq, mostFreqScore = score;
		}

		cout << '#' << tcNum << ' ' << mostFreqScore << '\n';
	}
}