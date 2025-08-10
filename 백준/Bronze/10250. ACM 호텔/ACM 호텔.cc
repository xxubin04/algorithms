#include <iostream>
#include <string>
using namespace std;

int tc;

int main() {
	cin >> tc;

	while (tc--) {
		int r, c, n;
		cin >> r >> c >> n;

		int floor = n % r;
		if (floor == 0) floor = r;

		int room = (n - 1) / r + 1;

		string ans = to_string(floor);
		if (room < 10) ans += "0";
		ans += to_string(room);

		cout << ans << '\n';
	}
}