#include <bits/stdc++.h>
using namespace std;

int main() {
	while (true) {
		int a, b, c;
		cin >> a >> b >> c;

		if (a + b + c == 0) break;
		if (a > b) swap(a, b);
		if (b > c) swap(b, c);
		if (a * a + b * b == c * c) cout << "right\n";
		else cout << "wrong\n";
	}
}