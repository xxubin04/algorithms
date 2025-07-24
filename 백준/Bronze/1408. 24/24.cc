#include <iostream>
#include <tuple>
#include <string>
#include <iomanip>
using namespace std;

int main() {
	int h1, m1, s1;
	int h2, m2, s2;
	char c = ':';

	cin >> h1 >> c >> m1 >> c >> s1;
	cin >> h2 >> c >> m2 >> c >> s2;

	int start = h1 * 3600 + m1 * 60 + s1;
	int end = h2 * 3600 + m2 * 60 + s2;

	if (end <= start)
		end += 24 * 3600;

	int diff = end - start;
	int dh = diff / 3600;
	int dm = (diff % 3600) / 60;
	int ds = diff % 60;

	cout << setfill('0');
	cout << setw(2) << dh << c
		<< setw(2) << dm << c
		<< setw(2) << ds << endl;

	return 0;
}