#include <bits/stdc++.h>
using namespace std;

string quad_tree(int** arr, int x, int y, int w) {
	bool mix_color = false; 
	int color = arr[x][y];   

	for (int i = x; i < x + w; i++) {
		for (int j = y; j < y + w; j++) {
			if (arr[i][j] != color) {
				mix_color = true;
				break;
			}
		}
		if (mix_color) break;
	}

	if (mix_color) {  
		string left_upper = quad_tree(arr, x, y, w / 2);
		string right_upper = quad_tree(arr, x, y + w / 2, w / 2);
		string left_lower = quad_tree(arr, x + w / 2, y, w / 2);
		string right_lower = quad_tree(arr, x + w / 2, y + w / 2, w / 2);

		return "(" + left_upper + right_upper + left_lower + right_lower + ")";
	} 
	return to_string(color);
}

int main() {
	int n;
	cin >> n;

	int** arr = new int* [n];

	for (int i = 0; i < n; i++) {
		arr[i] = new int[n];
		
		string line;
		cin >> line;

		for (int j=0; j<n; j++)
			arr[i][j] = line[j] - '0';
	}
	cout << quad_tree(arr, 0, 0, n) << '\n';
}