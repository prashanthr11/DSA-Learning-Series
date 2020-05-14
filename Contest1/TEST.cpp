#include <iostream>

using namespace std;

int main() {
    int a[100000], s = 0;
    int size = sizeof(a) / sizeof(a[0]);
    
    for(auto i = 0; i < size; ++i)
        cin >> a[i];
    
    for(auto i = 0; i < size; ++i)
        if(a[i] == 42)
            return 0;
        else
            std::cout << a[i] << std::endl;
}
