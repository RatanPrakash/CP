#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
    int t;
    cin >> t; // Read the number of test cases

    while (t--) {
        int n;
        cin >> n; // Read the length of the array
        vector<int> arr(n);

        for (int i = 0; i < n; ++i) {
            cin >> arr[i]; // Read the array elements
        }

        int ans = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                for (int k = 0; k < n; ++k) {
                    for (int l = 0; l < n; ++l) {
                        if (i != j && i != k && i != l && j != k && j != l && k != l) {
                            int temp = abs(arr[i] - arr[j]) + abs(arr[j] - arr[k]) + abs(arr[k] - arr[l]) + abs(arr[l] - arr[i]);
                            ans = max(ans, temp);
                        }
                    }
                }
            }
        }

        cout << ans << endl; // Print the answer
    }

    return 0;
}
