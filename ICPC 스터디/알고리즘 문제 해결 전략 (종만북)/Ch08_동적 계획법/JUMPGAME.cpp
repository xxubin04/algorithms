#include <bits/stdc++.h>
using namespace std;

int n, tc;
vector<vector<int>> grid;
int cache[100][100];

int jump(int x, int y) {
	if (x >= n || y >= n) return 0;

	if (x == n - 1 && y == n - 1) return 1;
	
	int& ret = cache[x][y];
	if (ret != -1) return ret;

	int jumpSize = grid[x][y];

	return ret = jump(x + jumpSize, y) || jump(x, y + jumpSize);
}

int main() {
	cin >> tc;

	while (tc--) {
		cin >> n;
		grid = vector<vector<int>>(n, vector<int>(n, 0));
		memset(cache, -1, sizeof(cache));

;		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> grid[i][j];
			}
		}

		if (jump(0, 0)) cout << "YES\n";
		else cout << "NO\n";
	}
}
