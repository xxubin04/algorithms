#include <iostream>
#include <vector>
using namespace std;

bool is_prime(int num) {
	for (int i = 2; i < num; i++) {
		if (num % i == 0) return false;
	}
	return true;
}

int main() {
	int n, cnt = 0;
	cin >> n;

	for (int i = 0; i < n; i++) {
		int num;
		cin >> num;

		if (is_prime(num) && num != 1) cnt++;
	}

	cout << cnt << '\n';
}