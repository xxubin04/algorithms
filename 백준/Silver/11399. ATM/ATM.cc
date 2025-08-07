#include <bits/stdc++.h>
using namespace std;

int n;
int arr[1000];

int main() {
	cin >> n;

	for (int i = 0; i < n; i++)
		cin >> arr[i];

	sort(arr, arr + n);

	int total = 0;
	for (int i = 0; i < n; i++)
		total += arr[i] * (n - i);

	cout << total << '\n';
}