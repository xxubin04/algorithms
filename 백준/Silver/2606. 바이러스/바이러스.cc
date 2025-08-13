#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int cnt = -1;
vector<int> visited(101, 0);
vector<vector<int>> v(101);

void dfs(int node) {
	if (visited[node] == 1) return;

	cnt++;
	visited[node] = 1;

	for (int i = 0; i < v[node].size(); i++) {
		dfs(v[node][i]);
	}
}

int main() {
	int num, con;
	cin >> num >> con;

	for (int i = 0; i < con; i++) {
		int a, b;
		cin >> a >> b;
		
		v[a].push_back(b);
		v[b].push_back(a);
	}

	dfs(1);
	cout << cnt << '\n';
}