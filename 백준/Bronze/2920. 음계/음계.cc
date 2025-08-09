#include <iostream>
#include <algorithm>
using namespace std;

int arr[8];

int main() {
   for (int i = 0; i < 8; i++) {
       cin >> arr[i];
   }

   int sort_arr[8];
   copy(begin(arr), end(arr), begin(sort_arr));
   sort(sort_arr, sort_arr + 8); 

   if (equal(begin(arr), end(arr), begin(sort_arr)))
       cout << "ascending" << '\n';
   else {
	   reverse(begin(sort_arr), end(sort_arr));

       if (equal(begin(arr), end(arr), begin(sort_arr)))
           cout << "descending" << '\n';
       else
           cout << "mixed" << '\n';
   }
}