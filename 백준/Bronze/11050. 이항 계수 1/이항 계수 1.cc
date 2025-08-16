#include <bits/stdc++.h>
using namespace std;

int main() {
	int n, k, total = 1;
	cin >> n >> k;

	for (int i = n; i > n - k; i--)
		total *= i;
	for (int i = k; i > 0; i--)
		total /= i;

	cout << total << '\n';
}