#include <bits/stdc++.h>
using namespace std;

int main() {
	int n, m, ans;
	cin >> n >> m;

	vector<int> v(n);

	for (int i = 0; i < n; i++) {
		cin >> v[i];
	}

	sort(v.begin(), v.end());

	int diff = 1e9;
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			for (int k = j + 1; k < n; k++) {
				int sum = v[i] + v[j] + v[k];
				if (abs(m - sum) < diff && sum <= m) {
					diff = abs(m - sum);
					ans = sum;
				}
			}
		}
	}

	cout << ans << '\n';
}