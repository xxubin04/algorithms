#include <bits/stdc++.h>
using namespace std;

int N, r, c;
int location = 0;

void find_location(int width) {
	if (width == 0) {
		return;
	}

	if (r < width) {
		if (c >= width) {  // 1사분면
			c -= width;
			location += (width * width);
		}
	}
	else {
		if (c < width) {  // 3사분면
			r -= width;
			location += (width * width * 2);
		}
		else {  // 4사분면 
			r -= width;
			c -= width;
			location += (width * width * 3);
		}
	}

	find_location(width / 2);
}

int main() {
	cin >> N >> r >> c;
	
	find_location(pow(2, N-1));
	cout << location << '\n';
}