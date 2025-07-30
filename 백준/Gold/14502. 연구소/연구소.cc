#include <bits/stdc++.h>  
using namespace std;  

int dx[] = { 1, -1, 0, 0 };  
int dy[] = { 0, 0, 1, -1 };  

vector<vector<int>> initial;
vector<pair<int, int>> virus; 
int max_safe_area = 0;  
int n, m;  

void spread_virus(vector<vector<int>>& tmp, int x, int y) {
   for (int i = 0; i < 4; i++) {  
       int nx = x + dx[i], ny = y + dy[i];  
       if (nx >= 0 && nx < n && ny >= 0 && ny < m) {  
           if (tmp[nx][ny] == 0) {
               tmp[nx][ny] = 2;
               spread_virus(tmp, nx, ny);
           }  
       }  
   }  
}  

void count_safe_area(vector<vector<int>>& tmp) {  
    for (auto& pos : virus) 
		spread_virus(tmp, pos.first, pos.second);
   
	int safe_area = 0;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if (tmp[i][j] == 0)
				safe_area++;

	max_safe_area = max(max_safe_area, safe_area);
}  
 
void build_wall(int cnt) {
    if (cnt == 3) {
        vector<vector<int>> tmp = initial;
        count_safe_area(tmp);
        return;
    }

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (initial[i][j] == 0) {
                initial[i][j] = 1;
                build_wall(cnt + 1);
                initial[i][j] = 0;
            }
}

int main() {  
   cin >> n >> m;
   initial.resize(n, vector<int>(m));

   for (int i = 0; i < n; i++)  
       for (int j = 0; j < m; j++) {  
           cin >> initial[i][j];
           if (initial[i][j] == 2)
               virus.push_back({i, j}); 
       }  

   build_wall(0);
   cout << max_safe_area << '\n';  
}