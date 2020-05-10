#include <iostream>
#include <map>
#include <climits>

using namespace std;

int main() {
        int n, k, maxi = INT_MIN, maxi2 = INT_MIN;
        map<string, string> a;
        map<string, int> b;
        map<string, int> c;
        cin >> n >> k;
        

        for(int i = 0; i < n; ++i) {
            string s, s2;
            cin >> s >> s2;
            a[s] = s2;
        }
        
        for(auto i:a) {
            b[i.first] = 0;
            c[i.second] = 0;
        }
        
        for(int i = 0; i < k; ++i) {
            string s;
            cin >> s;
            b[s]++;
            c[a[s]]++;
        }
        
        for(auto i:c)maxi = max(maxi, i.second);
        
        for(auto i:b)maxi2 = max(maxi2, i.second);
        
        for(auto i:c) {
            if(i.second == maxi) {
                cout << i.first << endl;
                break;
            }
        }
        
        for(auto i:b) {
            if(i.second == maxi2) {
                cout << i.first << endl;
                break;
            }
        }
}
