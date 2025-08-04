#include <bits/stdc++.h>
using namespace std;

int tc, num, total_cnt;
int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };

int main() {
	cin >> tc;
	cin.ignore();

	for (int i = 1; i <= tc; i++) {
		cin >> num;
		total_cnt = 0;
		vector<vector<int>> snail(num, vector<int>(num, 0));

		int x = 0, y = 0, dir = 0;
		for (int i = 1; i <= num * num; i++) {
			snail[x][y] = i;
			int nx = x + dx[dir], ny = y + dy[dir];

			if (nx < 0 || nx >= num || ny < 0 || ny >= num || snail[nx][ny] != 0) {
				dir = (dir + 1) % 4;
				nx = x + dx[dir], ny = y + dy[dir];
			}
			x = nx, y = ny;
		}

		cout << "#" << i << '\n';

		for (int i = 0; i < num; i++) {
			for (int j = 0; j < num; j++) {
				cout << snail[i][j] << ' ';
			}
			cout << '\n';
		}
	}
}
