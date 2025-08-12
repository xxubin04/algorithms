#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#define MAX 10001
using namespace std;

vector<vector<int>> graph(MAX);
vector<int> dfs_v;
vector<int> bfs_v;
vector<int> dfs_visited;
vector<int> bfs_visited;

void dfs(int node) {
	dfs_visited[node] = 1;
	dfs_v.push_back(node);
	
	for (int i : graph[node]) {
		if (dfs_visited[i] == 0)
			dfs(i);
	}
}

void bfs(int node) {
	queue<int> q;
	q.push(node);
	bfs_visited[node] = 1;

	while (!q.empty()) {
		int n = q.front();
		q.pop();
		bfs_v.push_back(n);
		
		for (int i : graph[n]) {
			if (bfs_visited[i] == 0) {
				q.push(i);
				bfs_visited[i] = 1;
			}
		}
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int n, m, v;
	cin >> n >> m >> v;

	
	dfs_visited.resize(n + 1, 0);
	bfs_visited.resize(n + 1, 0);

	int a, b;
	for (int i = 0; i < m; i++) {
		cin >> a >> b;

		graph[a].push_back(b);
		graph[b].push_back(a);
	}

	for (int i = 1; i <= n; i++) {
		sort(graph[i].begin(), graph[i].end());
	}
	
	dfs(v);
	bfs(v);

	for (size_t i = 0; i < dfs_v.size(); i++) {
		if (i) cout << " ";
		cout << dfs_v[i];
	}
	cout << '\n';
	for (size_t i = 0; i < bfs_v.size(); i++) {
		if (i) cout << " ";
		cout << bfs_v[i];
	}
}