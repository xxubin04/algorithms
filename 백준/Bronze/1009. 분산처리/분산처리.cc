#include <bits/stdc++.h>
using namespace std;

int main() {
	int tc;
	cin >> tc;

	for (int t = 0; t < tc; t++) {
		int a, b;
		cin >> a >> b;

		vector<int> v;
		
		a %= 10;
		if (a == 0) {
			cout << 10 << '\n';
			continue;
		}

		int i = a;
		while (true) {
			if (find(v.begin(), v.end(), i) != v.end()) {
				break;
			}
			v.push_back(i);
			i = (i * a) % 10;
		}
		cout << v[(b - 1) % v.size()] << '\n';
	}
}