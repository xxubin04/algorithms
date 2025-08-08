#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N, M, B;
int lowest_height = 256, highest_height = 0;

int main() {
	cin >> N >> M >> B;

	vector<vector<int>> ground(N, vector<int>(M, 0));

	int input;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> input;
			ground[i][j] = input;

			if (input < lowest_height) lowest_height = input;
			if (input > highest_height)	highest_height = input;
		}
	}

	int min_sec = 1e9;
	int ans_height = 0;
	for (int height = lowest_height; height <= highest_height; height++) {
		int copy_B = B, sec = 0;
		vector<pair<int, int>> lower_grounds;

		for (int x = 0; x < N; x++) {
			for (int y = 0; y < M; y++) {
				if (ground[x][y] == height) continue;
				else if (ground[x][y] > height) {
					copy_B += (ground[x][y] - height);
					sec += (ground[x][y] - height) * 2;
				}
				else {
					lower_grounds.push_back(make_pair(x, y));
				}
			}
		}

		bool success = true;  // 땅 고르기 성공 여부 
		for (auto& pos : lower_grounds) {
			int x = pos.first, y = pos.second;
			copy_B -= (height - ground[x][y]);
			if (copy_B < 0) success = false;  // 남는 블록이 없다면 
			sec += (height - ground[x][y]);
		}
		
		if (success && sec <= min_sec) {
			min_sec = sec;
			ans_height = height;
		}
	}
	cout << min_sec << " " << ans_height << '\n';
}