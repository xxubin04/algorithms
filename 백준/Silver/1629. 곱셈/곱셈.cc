#include <bits/stdc++.h>
using namespace std;

int a, b, c;
vector<int> v;

typedef long long ll;

ll sol(ll a, ll b, ll c) {
	if (b == 1) {
		return a % c;
	}

	ll temp = sol(a, b / 2, c);
	if (b % 2 == 0)
		return (temp * temp) % c;
	else
		return (temp * temp % c) * (a % c) % c;
}

int main() {
	cin >> a >> b >> c;

	cout << sol(a, b, c) << '\n';
}