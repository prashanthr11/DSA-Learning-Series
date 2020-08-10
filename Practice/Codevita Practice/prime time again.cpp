#include <bits/stdc++.h>

using namespace std;

bool isprime(int x) {
    if (x <= 1)
    return false;
    if (x <= 3)
    return true;
    if(x % 2 == 0 || x % 3 == 0)
    return false;
    int i = 5;
    while(i * i <= x) {
        if(x % i == 0 || x % (i + 2) == 0)
            return false;
        i += 6;
    }
    return true;
}

bool isprime_(int pre,int inc, int y) {
    while(pre < y) {
        if (isprime(pre)) {
            pre += inc;
        }
        else {
            return false;
        }
    }
    return true;
}


int solve(int a, int b) {
    int cnt = 0;
    if ((a > b) && (a % b) > -1) {
        int di = a / b; 
        for(auto i = 2; i < di; ++i) {
            if (isprime(i)) {
                int te = i;
                if(isprime_(te + di, di, a))
                    cnt++;
            }
        }
    }
    return cnt;
}





int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);cout.tie(NULL);
    
    int h, p;
    cin >> h >> p;
    cout << solve(h, p) << endl;
}
