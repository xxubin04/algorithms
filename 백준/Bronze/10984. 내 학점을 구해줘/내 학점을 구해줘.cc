#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	int tc;
	cin >> tc;

	for (int t = 0; t < tc; t++) {
		int n, total_c = 0;
		double total_g = 0;
		cin >> n;


		for (int i = 0; i < n; i++) {
			int c;
			double g;

			cin >> c >> g;

			total_c += c;
			total_g += c * g;
		}

		cout << total_c << " ";
		cout << fixed << setprecision(1) << (total_g / total_c) << '\n';
	}

	return 0;
}