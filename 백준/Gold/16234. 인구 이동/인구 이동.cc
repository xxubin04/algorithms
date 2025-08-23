#include <bits/stdc++.h>
using namespace std;

int n, l, r, total, day = 0;
vector<int> totals;
vector<vector<int>> v;
vector<vector<int>> visited;
vector<pair<int, int>> dirs = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };
vector<vector<pair<int, int>>> connection;

void bfs(int x, int y, int num) {
	queue<pair<int, int>> q;
	q.push({ x, y });
	total = v[x][y];
	visited[x][y] = 1;
	connection[num].push_back({ x, y });

	while (!q.empty()) {
		int x = q.front().first, y = q.front().second;
		q.pop();

		for (int d = 0; d < 4; d++) {
			int nx = x + dirs[d].first, ny = y + dirs[d].second;

			if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
			if (visited[nx][ny] == 1) continue;

			int diff = abs(v[x][y] - v[nx][ny]);
			if (diff < l || diff > r) continue;

			q.push({ nx, ny });
			visited[nx][ny] = 1;
			connection[num].push_back({ nx, ny });
			total += v[nx][ny];
		}
	}
}

int main() {
	cin >> n >> l >> r;

	v.assign(n, vector<int>(n, 0));

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> v[i][j];
		}
	}

	while (true) {
		
		int num = 0;
		connection.clear();
		totals.clear();
		visited.assign(n, vector<int>(n, 0));


		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (visited[i][j] == 0) {
					connection.push_back({});
					bfs(i, j, num);
					num++;
					totals.push_back(total);
				}
			}
		}

		if (num == n * n) break;

		for (int i = 0; i < connection.size(); i++) {
			for (int j = 0; j < connection[i].size(); j++) {
				int x = connection[i][j].first, y = connection[i][j].second;
				v[x][y] = totals[i] / connection[i].size();
			}
		}
		day++;
	}

	cout << day << '\n';
}