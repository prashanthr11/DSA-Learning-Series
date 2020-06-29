#include <bits/stdc++.h>

#define int long long

using namespace std;

signed main() {
    int t;
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        vector<int> a;
        for(auto i = 0; i < n; ++i) {
            int x;
            cin >> x;
            auto tmp = upper_bound(begin(a), end(a), x);
            if (tmp == a.end())
            a.push_back(x);
            else
            a[tmp - a.begin()] = x;
        }
        
        
        cout << a.size() << ' ';
        for(auto i:a)
        cout << i << ' ';
        cout << endl;
    }
}
