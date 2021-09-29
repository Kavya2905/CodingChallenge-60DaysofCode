#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'towerBreakers' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER m
 */

int main() {
    int i, t;
    cin >> t;
    
    while(t > 0){
        int n, m;
        cin >> n >> m;
        if(m == 1){
            cout << "2\n";
        }
        else if(n % 2 == 0){
            cout << "2\n";
        }
        else{
            cout << "1\n";
        }
        t--;
     
    }
    
    return 0;
}

