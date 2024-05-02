#include <iostream>
#include <vector>
using namespace std;

int main() {
    int t;
    cin >> t;  // number of test cases

    while (t--) {
        int n;
        cin >> n;  // size of the grid

        vector<string> grid(n);
        for (int i = 0; i < n; i++) {
            cin >> grid[i];
        }

        // solution
        vector<pair<int, int> > arr;
        for (int i = 0; i < n; i++) {
            int l = 0;
            int r = grid[0].size() - 1;
            int ct = 0;
            while (l < r && ct <= 2) {
                if (grid[i][l] != '1') {
                    l++;
                }
                if (grid[i][r] != '1') {
                    r--;
                }
                if (grid[i][l] == '1' && grid[i][r] == '1') {
                    arr.push_back(make_pair(l, r));
                    ct++;
                    break;
                }
            }
        }

        for (int i = 0; i < arr.size(); i++) {
            if (arr[i] == arr[i + 1]) {
                cout << "SQUARE" << endl;
            } else {
                cout << "TRIANGLE" << endl;
            }
            break;
        }
    }

    return 0;
}
