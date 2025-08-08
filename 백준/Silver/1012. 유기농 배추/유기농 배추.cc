#include <iostream>
#include <vector>
using namespace std;

int tc; 
int row, col, cabbage_cnt, worm = 0;
vector<vector<int>> visited;
vector<vector<int>> map;
vector<pair<int, int>> dir = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };

void dfs(int x, int y) {
	if (visited[x][y] == 1) return;
	visited[x][y] = 1;

	for (int d = 0; d < 4; d++) {
		int nx = x + dir[d].first, ny = y + dir[d].second;

		if (nx < 0 || nx >= row || ny < 0 || ny >= col) continue;
		if (map[nx][ny] == 1 && visited[nx][ny] == 0)
			dfs(nx, ny);
	}
}

int main() {
	cin >> tc;

	while (tc--) {
		cin >> row >> col >> cabbage_cnt; 

		map.assign(row, vector<int>(col, 0));
		visited.assign(row, vector<int>(col, 0));
		worm = 0;

		int x, y;
		for (int i = 0; i < cabbage_cnt; i++) {
			cin >> x >> y;
			map[x][y] = 1;
		}

		for (int i = 0; i < row; i++) {
			for (int j = 0; j < col; j++) {
				if (map[i][j] == 1 && visited[i][j] == 0) {
					dfs(i, j);
					worm++;
				}
			}
		}
		cout << worm << '\n';
	}
}