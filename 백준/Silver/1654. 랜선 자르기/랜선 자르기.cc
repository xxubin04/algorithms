#include <iostream>
#include <algorithm>
#include <array>
using namespace std;

typedef long long ll;

int main() {
	int have, need;
	array<int, 10000> arr;
	cin >> have >> need;
	
	for (int i = 0; i < have; i++)
		cin >> arr[i];

	ll max_length = 0;
	ll start = 1, last = *max_element(begin(arr), begin(arr) + have);
	while (start <= last) {
		ll cnt = 0;
		ll mid = (start + last) / 2;
		for (int i = 0; i < have; i++)
			cnt += (arr[i] / mid);
		
		if (cnt >= need) {
			max_length = max(max_length, mid);
			start = mid + 1;
		}
		else {
			last = mid - 1;
		}
	}

	cout << max_length << endl;
}