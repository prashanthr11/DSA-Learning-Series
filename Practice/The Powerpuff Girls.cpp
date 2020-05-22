#include <bits/stdc++.h>
#define int long long
using namespace std;
signed main(int argc, char *ar[])
{
    int t;
    cin >> t;
    vector<int> a(t), b(t), c(t);
    for(int i = 0; i < t; ++i) cin >> a[i];
    for(int i = 0; i < t; ++i) {
        cin >> b[i];
        c[i] = b[i] / a[i];
    }
    cout << *min_element(begin(c), end(c)) << endl;
}
