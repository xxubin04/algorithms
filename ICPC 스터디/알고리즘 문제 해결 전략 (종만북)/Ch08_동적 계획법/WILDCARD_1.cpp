#include <bits/stdc++.h>
using namespace std;

int tc;
int cache[101][101];
string W, S;

bool match(int w, int s) {
	int& ret = cache[w][s];
	if (ret != -1) return ret;

	while (w < W.size() && s < S.size() && (W[w] == '?' || W[w] == S[s])) {
		++w;
		++s;
	}

	// 문자열 W의 끝에 도달했다면
	if (w == W.size()) {  // 문자열 S의 끝에 도달했다면 매치됨
		if (s == S.size()) return ret = (s == S.size());  // 문자열 S의 끝에 도달하지 못한다면 매치안됨
	}

	if (W[w] == '*') {
		for (int i = 0; s + i <= S.size(); i++) {
			if (match(w + 1, s + i)) return ret = 1;
		}
	}
	return ret = 0;
}

int main() {
	cin >> tc;
	
	while (tc--) {
		cin >> W;

		int n;
		cin >> n;

		vector<string> result;

		while (n--) {
			cin >> S;

			memset(cache, -1, sizeof(cache));
			if (match(0, 0)) result.push_back(S);
		}
		sort(result.begin(), result.end());

		for (auto& r : result)
			cout << r << '\n';
	}
}
