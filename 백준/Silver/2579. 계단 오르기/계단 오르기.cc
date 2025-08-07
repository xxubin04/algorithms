#include <bits/stdc++.h>
using namespace std;

int dp[301];
int n;

int main() {
	cin >> n;
	vector<int> v(n);

	for (int i=0; i<n; i++)
		cin >> v[i];

	if (n >= 1) dp[0] = v[0];
	if (n >= 2) dp[1] = v[0] + v[1];
	if (n >= 3) dp[2] = max(v[0] + v[2], v[1] + v[2]);

	for (int i=3; i<n; i++)
		dp[i] = max(dp[i - 2] + v[i], dp[i - 3] + v[i] + v[i - 1]);

	cout << dp[n-1] << '\n';
}