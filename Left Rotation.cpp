#include <iostream>

using namespace std;


/*
 * Complete the 'rotateLeft' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER d
 *  2. INTEGER_ARRAY arr
 */

int main(){
    int n, d;
    cin >> n >> d;
    int a[n];
    for(int i = 0; i<n; i++){
        cin>>a[i];
        d %= n;
    }
    for(int i = d; i<n; i++){
        cout<<a[i]<<" ";
    }
    for(int i = 0; i < d; i++){
        cout<<a[i]<< " ";
    }
    return 0;
}
