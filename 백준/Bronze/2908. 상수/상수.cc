#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    string num_1, num_2;
    cin >> num_1 >> num_2;

    reverse(num_1.begin(), num_1.end());
    reverse(num_2.begin(), num_2.end());
    
    int int_num_1 = stoi(num_1);
    int int_num_2 = stoi(num_2);

    cout << max(int_num_1, int_num_2);

    return 0;
}