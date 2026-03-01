#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int t;  // number of test cases
    cin >> t;

    while (t--) {
        int l, r;
        cin >> l >> r;  // read l and r for each test case

        int ans = 0;

        double log_val = log2(l) / log2(3);
        ans += ceil(log_val);
        if (ans == log_val) {
            ans += 1;
        }
        ans += ans;

        for (int i = l + 1; i <= r; ++i) {
            double log_val = log2(i) / log2(3);
            if (ceil(log_val) == log_val) {
                ans += 1;
            }
            ans += ceil(log_val);
        }

        cout << ans << endl;
    }

    return 0;
}
