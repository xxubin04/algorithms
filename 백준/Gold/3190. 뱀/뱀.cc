#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, K, L, sec = 0;
vector<pair<int, int>> dir = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };
vector<pair<int, int>> apple;
vector<pair<int, char>> trans;
vector<pair<int, int>> snake = {make_pair(0, 0)};

int shift(int x, int y, int d) {
   // 방향 전환해야 하는지 확인
   auto it = find_if(trans.begin(), trans.end(), [](const pair<int, char>& t) {
       return t.first == sec;  // 현재의 시간과 일치하는지 확인 
       });
   
   if (it != trans.end()) {  // 방향 전환 해야한다면 
       if (it->second == 'L')  // 왼쪽으로 회전해야 한다면 
           d = (d + 3) % 4;
       else
           d = (d + 1) % 4;
   }

   int nx = x + dir[d].first, ny = y + dir[d].second;

   if (nx < 0 || nx >= N || ny < 0 || ny >= N) return ++sec;
   if (find(snake.begin(), snake.end(), make_pair(nx, ny)) != snake.end()) return ++sec;

   sec++;
   snake.push_back(make_pair(nx, ny)); // 뱀의 위치 추가 
    
   auto iter = find(apple.begin(), apple.end(), make_pair(nx, ny));

   // 이동할 위치에 사과가 없다면 길이 유지
   if (iter == apple.end())
       snake.erase(snake.begin());  // 뱀의 꼬리 제거
   else
       apple.erase(iter);

   return shift(nx, ny, d);
}

int main() {
   cin >> N >> K;

   int a, b;
   for (int i = 0; i < K; i++) {
       cin >> a >> b;
       apple.push_back(make_pair(a-1, b-1));
   }

   cin >> L;

   int x;
   char c;
   for (int i = 0; i < L; i++) { 
       cin >> x >> c;
       trans.push_back(make_pair(x, c));
   }

   cout << shift(0, 0, 0) << '\n'; 
}