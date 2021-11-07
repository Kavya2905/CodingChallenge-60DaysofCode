#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a, b;
    char ab, ba;
    cin >> a >> b;
    cout << a.size() << " " << b.size() << "\n";
    
    cout << a + b << "\n";
    
    ab = b[0];
    ba = a[0];
    a[0] = ab;
    b[0] = ba;
    
    // or swap(a[0], b[0]);
    cout << a << " " << b;
  
    return 0;
}
