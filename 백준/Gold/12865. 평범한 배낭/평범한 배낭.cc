#include <bits/stdc++.h>
using namespace std;

int n, k;
int arr[101][100001] = { 0 };

struct Thing {
	int weight, value;
};

int main() {
	cin >> n >> k;

	Thing thing[101];

	int w, v;

	for (int i = 1; i <= n; i++) {
		cin >> w >> v;

		thing[i] = { w, v };
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= k; j++) {
			int w = thing[i].weight, v = thing[i].value;

			if (w > j)
				arr[i][j] = arr[i - 1][j];
			else
				arr[i][j] = max(arr[i - 1][j], v + arr[i - 1][j - w]);
		}
	}

	cout << arr[n][k] << '\n';
	return 0;
}