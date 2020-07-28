#include <bits/stdc++.h>

#define ht(n) (int)ceil(log2(n))

using namespace std;

int n;

void build_segment_tree_optimal(int *arr, int *st) {
    for(auto i = 0; i < n; ++i)
        st[i + n] = arr[i];
        
    for(auto i = n - 1; i > 0; --i) 
        st[i] = st[i * 2] + st[i * 2 + 1];
}


int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8};
    n = sizeof(arr) / sizeof(arr[0]);
    int max_size = 2 * pow(2, ht(n));
    int st[max_size] = {0};
    build_segment_tree_optimal(arr, st);
}
