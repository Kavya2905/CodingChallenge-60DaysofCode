#include <iostream>
#include <cstdio>
using namespace std;

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max_of_four(int a,int b,int c,int d){
    int great;
    if(a>b && a>c && a>d){
        great = a;
    }
    else if(b>a && b>c && b>d){
        great = b;
    }
    else if(c>a && c>b && c>d){
        great = c;
    }
    else if(d>a && d>c && d>b){
        great = d;
    }
    return great;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}
