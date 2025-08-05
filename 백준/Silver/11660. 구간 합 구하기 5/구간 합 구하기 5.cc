#include <bits/stdc++.h>
using namespace std;

int n, m;
int arr[1025][1025];
int x1, y_1, x2, y2;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	cin >> n >> m;

	for (int a = 1; a <= n; a++) {
		for (int b = 1; b <= n; b++) {
			int num;
			cin >> num;
			arr[a][b] = arr[a][b] + arr[a - 1][b] + arr[a][b - 1] - arr[a - 1][b - 1] + num;
		}
	}

	for (int i = 0; i < m; i++) {
		cin >> x1 >> y_1 >> x2 >> y2;

		cout << arr[x2][y2] - arr[x1 - 1][y2] - arr[x2][y_1 - 1] + arr[x1 - 1][y_1 - 1] << '\n';
	}
}