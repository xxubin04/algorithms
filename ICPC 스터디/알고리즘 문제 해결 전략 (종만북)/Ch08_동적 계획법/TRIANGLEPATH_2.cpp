#include <bits/stdc++.h>
using namespace std;

int tc, triangle_size;
int triangle[101][101];
int cache[101][101];

int memo(int phase, int loc) {
	// base case - 마지막 단계라면 
	if (phase == triangle_size - 1) return triangle[phase][loc];

	// 이미 계산한 값이라면 바로 캐시된 값 반환 
	int& ret = cache[phase][loc];
	if (ret != -1) return ret;

	return ret = triangle[phase][loc] + max(memo(phase + 1, loc), memo(phase + 1, loc + 1));
}

int main() {
	cin >> tc;

	while (tc--) {
		cin >> triangle_size;

		memset(cache, -1, sizeof(cache));
		memset(triangle, 0, sizeof(triangle));

		for (int i = 0; i < triangle_size; i++) {
			for (int j = 0; j <= i; j++) {
				cin >> triangle[i][j];
			}
		}

		cout << memo(0, 0) << '\n';
	}
}
