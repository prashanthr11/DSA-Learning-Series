#include <bits/stdc++.h>

#define int long long

using namespace std;

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);cout.tie(NULL);
    
    int t;
    cin >> t;
    while(t--) {
        set<int> s, s1, s2;
        int n, sc, x, y;
        cin >> n >> sc >> x >> y;
        for(auto i = 1; i <= n; ++i)s.insert(i);
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
        set_difference(s.begin(), s.end(), s1.begin(), s1.end(), inserter(s2, s2.end()));
        cout << (s2.size() > sc? sc :s2.size());
        cout << endl;
    }
    return 0;
}
