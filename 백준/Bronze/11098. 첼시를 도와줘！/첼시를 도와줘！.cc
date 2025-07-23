#include <iostream>
#include <string>
using namespace std;

int main() {
	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		int p, cost, max_cost = 0;
		string player, max_player;
		cin >> p;

		for (int j = 0; j < p; j++) {
			cin >> cost >> player;

			if (cost > max_cost) {
				max_player = player, max_cost = cost;
			}
		}
		cout << max_player << "\n";
	}

	return 0;
}