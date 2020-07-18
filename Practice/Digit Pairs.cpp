#include <bits/stdc++.h>

using namespace std;

unordered_map<int, int> mp;

int getmax(int x) {
    int ans = 0;
    while(x) {
        ans =  max(ans, x % 10);
        x = x / 10;
    }
    return ans;
}



int getmin(int x) {
    int ans = 1e9;
    while(x) {
        ans =  min(ans, x % 10);
        x = x / 10;
    }
    return ans;
}

int solve(vector<int> x) {
    int cnt = 0, msb = 0;
    int sz = x.size();
    for(auto i = 0; i < sz; ++i) {
        msb = x[i] / 10;
        for(auto j = i + 1; j < sz; ++j) {
            if(msb == x[j] / 10 && mp[msb] < 2)
                mp[msb]++;
        }
    }
    for(auto i:mp)
        cnt += i.second;
    
    return cnt;
}


int main() {
    int n;
    cin >> n;
    
    
    vector<int> a(n), ans;
    for(int i = 0; i < n; ++i)
        cin >> a[i];
        
    for(auto i = 0; i < n; ++i) {
        int maxi = getmax(a[i]);
        int mini = getmin(a[i]);
        int x = (maxi * 11) + (mini * 7);
        ans.push_back(x % 100);
    }
    
    
    vector<int> e, o;
    
    for(auto i = 0; i < n; i = i + 2)
        e.push_back(ans[i]);

    for(auto i = 1; i < n; i = i + 2)
        o.push_back(ans[i]);


    int ret = solve(e) + solve(o);
    cout << ret << endl;

}