#include <bits/stdc++.h>

#define int long long

using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);cout.tie(NULL);
    
    int t;
    cin >> t;
    while(t--) {
        unordered_set<int> s1;
        int n, sc, x, y;
        cin >> n >> sc >> x >> y;
        for(auto i = 0; i < x; ++i) {
            int as;
            cin >> as;
            s1.insert(as);
        }
        for(auto i = 0; i < y; ++i) {
            int q;
            cin >> q;
            s1.insert(q);
        }
        int sz = s1.size();
        cout << min(n - sz, sc) << endl;
    }
    return 0;
}
