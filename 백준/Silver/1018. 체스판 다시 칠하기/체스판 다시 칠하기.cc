#include <bits/stdc++.h>
using namespace std;

int paint(const vector<string>& v, int r, int c, int start) {
	int cnt = 0;

	for (int i = 0; i < 8; i++) {
		for (int j = 0; j < 8; j++) {
			char color = ((i + j) % 2 == 0) ? start : (start == 'W' ? 'B' : 'W');
			if (v[r + i][c + j] != color) {
				cnt++;
			}
		}
	}
	return cnt;
}

int main() {
	int r, c;
	cin >> r >> c;

	vector<string> v(r);

	for (int i = 0; i < r; i++) {
		cin >> v[i];
	}

	int minCnt = 64;

	for (int i = 0; i <= r - 8; i++) {
		for (int j = 0; j <= c - 8; j++) {
			int cntW = paint(v, i, j, 'W');
			int cntB = paint(v, i, j, 'B');
			minCnt = min({minCnt, cntW, cntB});
		}
	}
	cout << minCnt << '\n';
}