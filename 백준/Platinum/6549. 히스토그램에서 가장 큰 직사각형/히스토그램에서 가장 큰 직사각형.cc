#include <bits/stdc++.h>
using namespace std;

long long arr[100001];

int main() {
	while (true) {
		int n;
		cin >> n;

		if (n == 0)
			break;

		stack<int> stk;
		long long max_extent = 0;
		
		for (int i = 0; i < n; i++)
			cin >> arr[i];

		for (int i = 0; i < n; i++) {
			while (!stk.empty() && arr[stk.top()] > arr[i]) {
				int arrTop = stk.top();
				stk.pop();

				long long width = stk.empty() ? i : i - stk.top() - 1;
				max_extent = max(max_extent, width * arr[arrTop]);
			}
			stk.push(i);
		}

		while (!stk.empty()) {
			long long arrTop = stk.top();
			stk.pop();

			long long width = stk.empty() ? n : n - stk.top() - 1;

			max_extent = max(max_extent, width * arr[arrTop]);
		}

		cout << max_extent << '\n';
	}
}