#include <bits/stdc++.h>

using namespace std;

struct Trie {
    struct Trie *root[26];
};


void create(struct Trie* head, string word) {
    auto tmp = head;
    for(auto i:word) {
        if (tmp -> root[i - 'a']) {
            tmp = tmp -> root[i - 'a'];
        }
        else {
            auto temp = new struct Trie();
            tmp -> root[i - 'a'] = temp;
            tmp = temp;
        }
    }
}


void print(struct Trie* tmp) {
    for (auto i = 0; i < 26; ++i) {
        if(tmp -> root[i]) {
            cout << char(i + 'a');
            print(tmp->root[i]);
        }
    }
}


int main() {
    int n;
    cin >> n;
    vector<string> v(n);
    
    for(auto i = 0; i < n; ++i)
        cin >> v[i];
        
    
    struct Trie *head = new struct Trie();
    
    
    for (auto i:v) {
        create(head, i);
    }
    
    auto tmp = head;
    print(tmp);
 
}
