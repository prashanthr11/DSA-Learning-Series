#include <bits/stdc++.h>
#include <iomanip>
#include <string.h>
#include <ctype.h>

using namespace std;

int main() {
    int n, k, cnt = 0;
    priority_queue<int> q;
    cin >> k >> n;


    for(int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        if (x == 0) {
            cout << "Invalid Input" << endl;
            return 0;
        }
        q.push(x);
    }

    while(k >= q.top() && q.top() > 0) {
        if (q.size()) {
            int temp = q.top();
            k = k - (temp % 2) - (temp / 2);
            // cout << k << endl;
            q.pop();
        }
        else
            break;
    }
    
    // cout << k << endl;
    
    if(q.size())
        cout << "NO" << endl;
    else
        cout << "YES" << endl;
}
