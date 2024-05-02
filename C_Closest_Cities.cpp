#include <iostream>
#include <vector>

using namespace std;

int main() {
    int numTestCases;
    cin >> numTestCases;

    for (int testCase = 0; testCase < numTestCases; ++testCase) {
        int n;
        cin >> n;
        vector<int> arr(n);
        for (int i = 0; i < n; ++i) {
            cin >> arr[i];
        }

        vector<int> distances(n - 1);
        for (int i = 0; i < n - 1; ++i) {
            distances[i] = abs(arr[i + 1] - arr[i]);
        }

        int m;
        cin >> m;

        for (int query = 0; query < m; ++query) {
            int x, y;
            cin >> x >> y;
            --x;
            --y;

            int ans = 0;
            while (x != y) {
                if (x < y) { // going right
                    if (x == 0) {
                        ans += 1;
                        x += 1;
                    } else if (distances[x] < distances[x - 1]) {
                        ans += 1;
                        x += 1;
                    } else {
                        ans += distances[x];
                        x += 1;
                    }
                } else {
                    if (x == n - 1) {
                        ans += 1;
                        x -= 1;
                    } else if (distances[x - 1] < distances[x]) {
                        ans += 1;
                        x -= 1;
                    } else {
                        ans += distances[x - 1];
                        x -= 1;
                    }
                }
            }
            cout << ans << endl;
        }
    }

    return 0;
}
