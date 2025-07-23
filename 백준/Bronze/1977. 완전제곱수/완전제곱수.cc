#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int main() {
	int m, n;
	int total = 0, num = 0;
	vector<int> v;

	cin >> m;
	cin >> n;
	
	for (int i = ceil(sqrt(m)); i <= sqrt(n); i++) {
		num = pow(i, 2);
		v.push_back(num);
		total += num;
	}

	if (total == 0) {
		cout << -1 << endl;
	}
	else {
		cout << total << endl;
		cout << v.front() << endl;
	}
	
	return 0;
}