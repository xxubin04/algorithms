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
queue<int> q;

void dfs(int node) {
	dfs_visited[node] = 1;
	dfs_v.push_back(node);
	
	for (int i : graph[node]) {
		if (dfs_visited[i] == 0)
			dfs(i);
	}
}

void bfs(int node) {
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

	q.push(v);
	bfs_visited[v] = 1;
	bfs(v);

	for (auto node : dfs_v)
		cout << node << " ";

	cout << "\n";

	for (auto node : bfs_v)
		cout << node << " ";
}