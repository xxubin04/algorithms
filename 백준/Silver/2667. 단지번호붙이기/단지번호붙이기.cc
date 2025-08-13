#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int n, cnt;
vector<vector<int>> v;
vector<vector<int>> visited;
vector<pair<int, int>> dir = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };

void dfs(int x, int y, int num) {
	if (x < 0 || x >= n || y < 0 || y >= n || v[x][y] != -1) return;

	cnt++;
	v[x][y] = num;
	for (int i = 0; i < 4; i++) {
		int nx = x + dir[i].first, ny = y + dir[i].second;
		dfs(nx, ny, num);
	}
}

int main() {
	cin >> n;

	v.assign(n, vector<int>(n, 0));
	vector<int> areas;

	string line;
	for (int i = 0; i < n; i++) {
		cin >> line;

		for (int j = 0; j < n; j++) {
			if (line[j] - '0' == 1)
				v[i][j] = -1;
			else
				v[i][j] = 0;
		}
	}

	int num = 0;
	for (int x = 0; x < n; x++) {
		for (int y = 0; y < n; y++) {
			if (v[x][y] == -1) {
				cnt = 0;
				dfs(x, y, num++);
				areas.push_back(cnt);
			}
		}
	}

	sort(areas.begin(), areas.end());
	cout << num << '\n';
	for (int i = 0; i < areas.size(); i++) {
		if (i != 0) cout << "\n";
		cout << areas[i];
	}
}