#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        // TODO: Add your code here
        sort(a.begin(), a.end());
        vector<int> diff(n-1);
        for (int i = 1; i < n; i++) {
            diff[i-1] = a[i] - a[i-1];
        }

        // for (int i = 0; i < n-1; i++) {
        //     cout << diff[i] << " ";
        // }

        int s = 0;
        for (int i = 0; i < n-1; i++) {
            s = s + diff[i];
        }
        cout << s << endl;


    }

    return 0;
}
