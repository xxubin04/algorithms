#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	int n;
	cin >> n;

	for (int i = n; i > 0; i--) {
		string stars;

		for (int s = n; s > 0; s--)
			stars += (s <= i) ? "*" : " ";

		cout << stars << "\n";
	}

	return 0;
}