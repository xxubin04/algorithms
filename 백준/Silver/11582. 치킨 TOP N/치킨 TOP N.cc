#include <bits/stdc++.h>
using namespace std;

int main() {
	int N, K;
	cin >> N;
	vector<int> chicken(N);

	for (int i = 0; i < N; i++) {
		cin >> chicken[i];
	}

	cin >> K;

	for (int i = 0; i < K; i++) {
		int start = i * (N / K);
		int end = start + (N / K);

		sort(chicken.begin() + start, chicken.begin() + end);
	}

	for (int i = 0; i < N; i++)
		cout << chicken[i] << " ";

	return 0;
}