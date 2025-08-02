#include <bits/stdc++.h>
using namespace std;

int tc, triangle_size;
int cache[101][101];

void memo(int phase, int loc) {
	if (loc == 0)  // 각 단계에서의 위치가 0일 때 
		cache[phase][loc] += cache[phase - 1][loc];
	else if (loc == phase)  // 각 단계에서의 위치가 마지막일 때 
		cache[phase][loc] += cache[phase - 1][loc - 1];
	else
		cache[phase][loc] += max(cache[phase - 1][loc - 1], cache[phase - 1][loc]);
}

int main() {
	cin >> tc;

	memset(cache, -1, sizeof(cache));  // 캐시 -1로 초기화 

	while (tc--) {
		cin >> triangle_size;

		for (int i = 0; i < triangle_size; i++) {
			for (int j = 0; j <= i; j++) {
				cin >> cache[i][j];
			}
		}

		for (int phase = 1; phase < triangle_size; phase++) {  // 각 단계와 위치마다 최댓값으로 메모이제이션 
			for (int loc = 0; loc <= phase; loc++) {
				memo(phase, loc);
			}
		}

		int max_sum = 0;
		for (auto& i : cache[triangle_size - 1]) {  // 마지막 단계에서의 최댓값 출력 
			if (i > max_sum) max_sum = i;
		}

		cout << max_sum << '\n';
	}
}
