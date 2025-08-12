#include <iostream>
#include <vector>
#include <queue>
using namespace std;
#define INF 1e9

int n, m;
vector<vector<int>> maze;
vector<pair<int, int>> dir = { {0,1}, {1,0}, {0,-1}, {-1,0} };

int bfs() {
	queue<pair<int, int>> q;
	q.push(make_pair(0, 0));
	maze[0][0] = 1;

	while (!q.empty()) {
		int x, y;
		x = q.front().first, y = q.front().second;
		q.pop();

		if (x == n - 1 && y == m - 1) {
			return maze[x][y];
		}

		for (int d = 0; d < 4; d++) {
			int nx = x + dir[d].first;
			int ny = y + dir[d].second;
			if (nx >= 0 && nx < n && ny >= 0 && ny < m && maze[nx][ny] == INF) {
				q.push(make_pair(nx, ny));
				maze[nx][ny] = maze[x][y] + 1;
			}
		}
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n >> m;

	maze.resize(n, vector<int>(m, 0));

	for (int i = 0; i < n; i++) {
		string line;
		cin >> line;

		for (int j = 0; j < m; j++) {
			if (line[j] - '0' == 1)
				maze[i][j] = INF;
			else
				maze[i][j] = 0;
		}
	}

	cout << bfs() << '\n';
}