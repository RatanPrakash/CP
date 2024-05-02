#include <iostream>
#include <vector>
#include <deque>

using namespace std;

int main() {
    int t;
    cin >> t; // number of test cases

    for (int i = 0; i < t; ++i) {
        int n;
        cin >> n; // length of the lost string

        vector<int> trace(n);
        for (int j = 0; j < n; ++j) {
            cin >> trace[j]; // trace of the string
        }

        vector<deque<char> > dic(1, deque<char>(1, 'a'));
        char ch = 'a';
        string ans = "a";
        for (int j = 1; j < n; ++j) {
            if (trace[j] == 0) {
                ch = ch + 1;
                ans += ch;
                dic[0].push_back(ch);
            } else {
                if (!dic[trace[j] - 1].empty()) {
                    ans += dic[trace[j] - 1][0];
                    dic[trace[j]].push_back(dic[trace[j] - 1][0]);
                    dic[trace[j] - 1].pop_front();
                }
            }
        }
        cout << ans << endl;
    }

    return 0;
}
