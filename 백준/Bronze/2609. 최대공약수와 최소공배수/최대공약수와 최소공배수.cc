#include <iostream>  
#include <numeric>  

using namespace std;  

int main() {  
	int a, b;  
	cin >> a >> b;  

	cout << gcd(a, b) << '\n';  
	cout << lcm(a, b) << '\n';

	return 0;
}