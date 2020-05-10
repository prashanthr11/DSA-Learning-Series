#include <iostream>
#include <queue>

using namespace std;

int main() {
    int t;
    cin >> t;
    while(t--) {
        int n, k, cnt = 0;
        priority_queue<int> q;
        cin >> n >> k;
        

        for(int i = 0; i < n; ++i) {
            int x;
            cin >> x;
            q.push(x);
        }
        
        
        while(k > 0 && q.top() > 0) {
            int temp = q.top();
            k -= temp;
            q.pop();
            q.push(temp / 2);
            ++cnt;
        }
        if(k > 0)
        cout << "Evacuate" << endl;
        else
        cout << cnt << endl;
    }
}
