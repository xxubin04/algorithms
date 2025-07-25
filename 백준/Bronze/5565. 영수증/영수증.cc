#include <iostream>
using namespace std;

int main() {
	int total = 0;
	int price;
	cin >> price;

	for (int i = 0; i < 9; i++) {
		int p;
		cin >> p;

		total += p;
	}

	cout << price - total << '\n';

	return 0;
}