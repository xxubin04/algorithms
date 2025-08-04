#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int tc;

int main() {
	int cnt = 0;
	cin >> tc;

	while (true) {
		if (cnt == tc) break;

		cnt++;
		int n;
		cin >> n;

		vector<int> v(n, 0);

		for (int i = 0; i < n; i++)
			cin >> v[i];

		int max_price = 0;
		ll ans = 0;
		for (int j = n - 1; j >= 0; j--) {
			if (v[j] >= max_price)
				max_price = v[j];
			ans += (max_price - v[j]);
		}
		cout << '#' << cnt << ' ' << ans << '\n';
	}
}
