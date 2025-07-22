#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int n;
vector<vector<int>> w;

int tsp(int i, vector<int>& visited, int cost) {
	int min_cost = INT_MAX;

	bool all_visited = true;
	for (int v : visited) {
		if (v == 0) {
			all_visited = false;
			break;
		}
	}

	if (all_visited) {
		if (w[i][0] != 0) {
			return cost + w[i][0];
		}
		else {
			return INT_MAX;
		}
	}

	for (int j = 0; j < n; j++) {
		if (visited[j] == 0 && w[i][j] != 0) {
			visited[j] = 1;
			min_cost = min(min_cost, tsp(j, visited, cost + w[i][j]));
			visited[j] = 0;
		}
	}

	return min_cost;
}

int main() {
	cin >> n;
	w.resize(n, vector<int>(n));

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			cin >> w[i][j];

	vector<int> visited(n, 0);
	visited[0] = 1;

	int result = tsp(0, visited, 0);
	cout << result << endl;

	return 0;
}