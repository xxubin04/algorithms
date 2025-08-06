#include <bits/stdc++.h>
using namespace std;
#define INF int(1e9)

int n;
int dp[100'001];

int main() {
	cin >> n;

	fill(dp, dp+100'001, INF);
	dp[0] = 0;

	for (int i=1; i<=n; i++) {
		int k = 0;
		while (k <= i) {
			if (k * k > i) break;
			dp[i] = min(dp[i - k * k] + 1, dp[i]);
			k++;
		}
	}
	cout << dp[n] << '\n';
}