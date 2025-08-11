#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int MAX = 100000;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n, k;
	cin >> n >> k;

	vector<int> dist(MAX + 1, -1);
	queue<int> q;

	dist[n] = 0;
	q.push(n);

	while (!q.empty()) {
		int x = q.front();
		q.pop();

		if (x == k) break;

		int next_pos[3] = { x * 2, x + 1, x - 1 };
		for (int np : next_pos) {
			if (0 <= np && np <= MAX && dist[np] == -1) {
				dist[np] = dist[x] + 1;
				q.push(np);
			}
		}
	}
	cout << dist[k] << '\n';
}