#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    int t;
    cin >> t; // Read the number of test cases

    for (int testCase = 0; testCase < t; ++testCase) {
        int n, m;
        cin >> n >> m; // Read n and m

        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i]; // Read the elements of the array
        }

        string s;
        cin >> s; // Read the string s

        // Solution
        long long prod = 1;
        for (int num : a) { // Calculate the product of elements in the array
            prod *= num;
        }

        vector<int> ans;
        int r = -1;
        int l = 0;
        for (char command : s) {
            ans.push_back(prod % m);
            if (command == 'R') {
                prod /= a[r];
                r -= 1;
            } else {
                prod /= a[l];
                l += 1;
            }
        }

        for (int num : ans) {
            cout << num << " ";
        }
        cout << endl;
    }

    return 0;
}
