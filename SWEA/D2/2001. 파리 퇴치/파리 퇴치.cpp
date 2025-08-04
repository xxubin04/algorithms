#include <bits/stdc++.h>
using namespace std;

int tc, n, m;

int main() {
	cin >> tc;

	for (int t = 1; t <= tc; t++) {
		cin >> n >> m;
		cin.ignore();

		vector<vector<int>> v(n, vector<int>(n));
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> v[i][j];
			}
		}

		int maxTotal = 0;
		for (int startX = 0; startX <= n - m; startX++) {
			for (int startY = 0; startY <= n - m; startY++) {
				int total = 0;
				for (int i = 0; i < m; i++) {
					for (int j = 0; j < m; j++) {
						total += v[startX+i][startY+j];
					}
				}
				if (total > maxTotal)
					maxTotal = total;
			}
		}
		cout << "#" << t << ' ' << maxTotal << '\n';
	}
}