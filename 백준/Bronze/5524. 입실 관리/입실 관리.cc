#include <iostream>

using namespace std;

int main() {
    int num;
    cin >> num;

    string word;

    for (int i=0; i<num; i++) {
        cin >> word;
        for (int j = 0; j < word.size(); j++) {
            if ('A' <= word[j] && word[j] <= 'Z')
                word[j] += 32;    
            cout << word[j];
        }
        cout << endl;
    }
    return 0;
}