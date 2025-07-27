#include <bits/stdc++.h>
using namespace std;

int n;
vector<vector<char>> stars;

void middle_blank(int x, int y, int length) {
	if (length == 1)
		return;

	length /= 3;
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			for (int a = length; a < 2 * length; a++) {
				for (int b = length; b < 2 * length; b++) {
					stars[x + a][y + b] = ' ';
				}
			}
			middle_blank(x + i * length, y + j * length, length);
		}
	}
}

int main() {
	cin >> n;

	stars.resize(n, vector<char>(n, '*'));

	middle_blank(0, 0, n);

	for (int i = 0;i < n; i++) {
		for (int j = 0; j < n; j++) {
			cout << stars[i][j];
		}
		cout << endl;
	}

	return 0;
}