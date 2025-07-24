#include <iostream>
#include <vector>
#include <tuple>
using namespace std;

int main() {
	int n;
	cin >> n;

	vector<tuple<string, int, int, int>> vt;

	for (int i = 0; i < n; i++) {
		string name;
		int day, month, year;

		cin >> name >> day >> month >> year;

		vt.push_back(make_tuple(name, day, month, year));
	}

	tuple<string, int, int, int> youngest = vt[0];
	tuple<string, int, int, int> oldest = vt[0];

	for (int i = 1; i < n; i++) {

		if (tie(get<3>(vt[i]), get<2>(vt[i]), get<1>(vt[i]))
			< tie(get<3>(youngest), get<2>(youngest), get<1>(youngest))) {
			youngest = vt[i];
		}
		if (tie(get<3>(vt[i]), get<2>(vt[i]), get<1>(vt[i]))
			> tie(get<3>(oldest), get<2>(oldest), get<1>(oldest))) {
			oldest = vt[i];
		}
	}

	cout << get<0>(oldest) << "\n";
	cout << get<0>(youngest) << "\n";

	return 0;
}