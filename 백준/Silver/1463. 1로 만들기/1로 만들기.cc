#include <bits/stdc++.h>
using namespace std;
#define INF 1e9

int dp[1'000'001];

 void sol(int n) {
	 if (n == 1) return;
	 if (dp[n] != INF) return; // 이미 계산된 경우

	 sol(n - 1);
	 dp[n] = min(dp[n - 1] + 1, dp[n]); // 1을 빼는 경우

	 if (n % 3 == 0) {
		 sol(n / 3);
		 dp[n] = min(dp[n / 3] + 1, dp[n]); // 3으로 나누는 경우
	 }

	 if (n % 2 == 0) {
		 sol(n / 2);
		 dp[n] = min(dp[n / 2] + 1, dp[n]); // 2로 나누는 경우
	}
}

int main() {
	int n;
	cin >> n;

	fill(dp, dp + 1'000'001, INF);
	dp[0] = 0, dp[1] = 0;

	sol(n);

	cout << dp[n] << '\n';
}