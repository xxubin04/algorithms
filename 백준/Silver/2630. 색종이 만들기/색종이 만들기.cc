#include <bits/stdc++.h>
using namespace std;

int white = 0, blue = 0;

string check_color(int** arr, int x, int y, int w) {
	bool mix_color = false;
	string color = arr[x][y] == 0 ? "white" : "blue";
	
	for (int i = x; i < x + w; i++) {
		for (int j = y; j < y + w; j++) {
			if (arr[i][j] == 1) {  // 흰, 파 섞여있을 때 
				if (color == "white") {
					mix_color = true;
					return "mix";
				}
			}
			else {  // 파, 흰 섞여있을 때
				if (color == "blue") {
					mix_color = true;
					return "mix";
				}
			}
		}
	}
	return color;
}

void sol(int** arr, int x, int y, int w) {
	if (w == 1) {  // 1x1 크기일 때 
		if (arr[x][y] == 0)
			white++;
		else
			blue++;
		return;
	}

	string color = check_color(arr, x, y, w);

	if (color == "mix") {
		for (int i = 0; i < 2; i++)
			for (int j = 0; j < 2; j++)
				sol(arr, x + i * (w / 2), y + j * (w / 2), w / 2);
	}
	else if (color == "white")
		white++;
	else blue++;
}

int main() {
	int w;
	cin >> w;
	cin.ignore();

	int** arr = new int* [w];  // 동적 배열 생성 

	for (int i = 0; i < w; i++) {
		arr[i] = new int[w];
		for (int j = 0; j < w; j++) {
			cin >> arr[i][j];
		}
	}

	sol(arr, 0, 0, w);

	cout << white << '\n' << blue << '\n';
}