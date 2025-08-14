#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n, a, b, r;
vector<vector<int>> relation;
vector<int> visited;

int bfs(int p) {
	queue<int> q;
	q.push(p);
	visited[p] = 0;

	while (!q.empty()) {
		int person = q.front();
		q.pop();

		for (int i = 0; i < relation[person].size(); i++) {
			if (visited[relation[person][i]] != 0) continue;
			q.push(relation[person][i]);
			visited[relation[person][i]] = visited[person] + 1;
		}
	}

	if (visited[b] == 0) return -1;
	else return visited[b];
}

int main() {
	cin >> n >> a >> b >> r;

	relation.assign(n + 1, vector<int>());
	visited.assign(n + 1, 0);

	int c, d;
	for (int i = 0; i < r; i++) {
		cin >> c >> d;
		relation[c].push_back(d);
		relation[d].push_back(c);
	}

	cout << bfs(a) << '\n';
}