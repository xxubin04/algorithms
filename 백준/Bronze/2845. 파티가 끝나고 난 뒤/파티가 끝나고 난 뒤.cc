#include <iostream>

using namespace std;

int main() {
    int L = 0, P = 0;
    int array[5];

    cin >> L >> P;
    for (int i=0; i<5; i++)
        cin >> array[i];

    for (int i=0; i<5; i++)
        cout << array[i]-(L*P) << " ";

    return 0;
}