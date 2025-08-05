#include <bits/stdc++.h>
using namespace std;

int n, k;

int main() {
	cin >> n >> k;

	vector<vector<int>> dp(n+1, vector<int>(k+1));

	int weight, value;
	vector<pair<int, int>> vec;

	vec.push_back(make_pair(0, 0));

	for (int i = 1; i <= n; i++) {
		cin >> weight >> value;

		vec.push_back(make_pair(weight, value));
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= k; j++) {
			int w = vec[i].first, v = vec[i].second;

			if (w > j)
				dp[i][j] = dp[i - 1][j];
			else
				dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w]);
		}
	}

	cout << dp[n][k] << '\n';
	return 0;
}
