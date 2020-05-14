#include <iostream>
#include <unordered_map>
#include <bits/stdc++.h>
using namespace std;


int main() {
    int t;
    cin >> t;
    while(t--) {
        string s;
        unordered_map<char, int> mp;
        cin >> s;
        
        if(s.length() % 2 == 0) {
            for(int i = 0; i < s.length() / 2; ++i) 
                mp[s[i]]++;
            
            for(int i = s.length()/2; i < s.length(); ++i) 
                mp[s[i]]--;
        }
        else {
            for(int i = 0; i < floor(s.length() / 2); ++i) 
                mp[s[i]]++;
            
            for(int i = floor(s.length() / 2) + 1; i < s.length(); ++i) 
                mp[s[i]]--;
        }
        
        bool flag = true;
        
        for(auto i:mp) {
            if(i.second != 0) {
                flag = false;
                break;
            }
        }
        
        if(flag)cout << "YES" << endl;
        else cout << "NO" << endl;
        
    }
}
