#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'hourglassSum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */



int main()
{
   int p, q, a[10][10], s = 0;
    for(int i = 0; i < 6; i++){
        for(int j = 0; j < 6; j++)
        cin>> a[i][j];
    }  
    
    for(int i = 0; i < 6; i++){
        for(int j = 0; j < 6; j++){
            if(j+2 < 6 && i+2 < 6){
                int sum; 
                sum = a[i][j] + a[i][j+1] + a[i][j+2]+ a[i+1][j+1] +
                a[i+2][j] + a[i+2][j+1] + a[i+2][j+2];
                
                if(sum > s){
                    s = sum; // looping through each of the sums  and finding the maximum
                }
            }
            
        }
    } 
    cout << s; 
    return 0;


}
