#include <bits/stdc++.h>
using namespace std;

int tc;
int dp[100'001] = { 0 };

int main() {
	cin >> tc;

	dp[1] = 1, dp[2] = 2, dp[3] = 4;

	while (tc--) {
		int n;
		cin >> n;

		for (int i = 0; i <= n; i++) {
			if (i >= 4 && dp[i] == 0) {
					dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
				}
			}
		cout << dp[n] << '\n';
	}
}