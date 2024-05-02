#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int MEX(vector<int>& a) {
    sort(a.begin(), a.end());
    int mex = 0;
    for (int i : a) {
        if (i == mex) {
            mex++;
        }
    }
    return mex;
}

int new_MEX(int x, vector<int>& arr, int prev_mex) {
    if (x == prev_mex) {
        vector<int> temp = arr;
        temp.push_back(x);
        return MEX(temp);
    }
    if (prev_mex == 0) {
        return 0;
    }
    if (x > prev_mex) {
        return prev_mex;
    }
}

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

        vector<int> p;

        if (a[0] > 0) {
            p.push_back(0);
        } else {
            p.push_back(-a[0]);
        }

        int prev_mex = MEX(p);
        for (int i = 1; i < n; i++) {
            int newx;
            if (a[i] >= 1) {
                newx = prev_mex;
                p.push_back(newx);
                prev_mex = new_MEX(newx, p, prev_mex);
            } else {
                newx = prev_mex - a[i];
                p.push_back(newx);
                prev_mex = new_MEX(newx, p, prev_mex);
            }
        }
        
        for (int i = 0; i < n; i++) {
            cout << p[i] << " ";
        }
        cout << endl;
    }

    return 0;
}
