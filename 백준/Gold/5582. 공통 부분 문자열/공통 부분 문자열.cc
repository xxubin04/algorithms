#include <bits/stdc++.h>
using namespace std;

string str1, str2;
int dp[4001][4001];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> str1 >> str2;

	memset(dp, 0, sizeof(dp));

	int ans = 0;

	for (int i = 1; i <= str1.length(); i++) {
		for (int j = 1; j <= str2.length(); j++) {
			char char1 = str1[i-1];
			char char2 = str2[j-1];

			if (char1 == char2) {
				dp[i][j] = dp[i - 1][j - 1] + 1;
				ans = max(ans, dp[i][j]);
			}
			else {
				dp[i][j] = 0;
			}
		}
	}

	cout << ans << '\n';
}