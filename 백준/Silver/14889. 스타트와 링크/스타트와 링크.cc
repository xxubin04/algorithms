#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> result;

void combination(vector<int>& arr, vector<int>& comb, int start, int r) {
    if (r == 0) {
        result.push_back(comb);
        return;
    }

    for (int i = start; i < arr.size(); ++i) {
        comb.push_back(arr[i]);
        combination(arr, comb, i + 1, r - 1);
        comb.pop_back();
    }
}

int main() {
    int n;
    cin >> n;

    vector<int> arr;
    vector<vector<int>> capacity(n, vector<int>(n, 0));

    for (int i = 0; i < n; i++)
        arr.push_back(i);

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> capacity[i][j];

    vector<int> comb;
    combination(arr, comb, 0, n / 2);

    int min_gap = 1e9;

    for (int i = 0; i < result.size() / 2; i++) {
        vector<int> team1 = result[i];
        vector<bool> in_team(n, false);
        for (int x : team1) in_team[x] = true;

        vector<int> team2;
        for (int j = 0; j < n; j++) {
            if (!in_team[j]) team2.push_back(j);
        }

        int team1_score = 0, team2_score = 0;

        for (int a = 0; a < team1.size(); a++) {
            for (int b = a + 1; b < team1.size(); b++) {
                team1_score += capacity[team1[a]][team1[b]] + capacity[team1[b]][team1[a]];
            }
        }

        for (int a = 0; a < team2.size(); a++) {
            for (int b = a + 1; b < team2.size(); b++) {
                team2_score += capacity[team2[a]][team2[b]] + capacity[team2[b]][team2[a]];
            }
        }

        min_gap = min(min_gap, abs(team1_score - team2_score));
    }

    cout << min_gap << '\n';
}