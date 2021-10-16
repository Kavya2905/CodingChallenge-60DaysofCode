#include <bits/stdc++.h>
#include <iostream>
using namespace std;

/*
 * Complete the 'dynamicArray' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. 2D_INTEGER_ARRAY queries
 */

int main(){
    int n, q, lastAns = 0;
    cin >> n >> q;
    vector < vector <int>> a(n);
    int seq;
    int pos;
    int type, x, y;
    for(int i = 0; i<q; i++){
        cin >> type >> x >> y;
        seq = ((x ^ lastAns) % n);
        if(type == 1){
            a[seq].push_back(y);
        }
        else if(type == 2){
            pos = (y % a[seq].size());
            lastAns = a[seq][pos];
            cout<< lastAns<< "\n";
            
        }
    }
    return 0;
}
