#include <bits/stdc++.h>
using namespace std;

int main() {
	int n, tshirt, pen, purchase_t = 0, purchase_p;
	int arr[6];
	cin >> n;
	cin >> arr[0] >> arr[1] >> arr[2] >> arr[3] >> arr[4] >> arr[5];
	cin >> tshirt >> pen;

	for (int i = 0; i < 6; i++) {
		purchase_t += (ceil(double(arr[i]) / tshirt));
	}
	cout << purchase_t << '\n' << n / pen << " " << n % pen << '\n';
}