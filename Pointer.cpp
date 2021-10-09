#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int a,b, *p, *q, *one, diff;
    cin >> a;
    cin >> b;
    
    p = &a;
    q = &b;
    
    cout << *p + *q<< "\n";
    diff = abs(*p - *q);
    cout << diff;
    return 0;
}
