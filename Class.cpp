#include <iostream>
#include <sstream>
using namespace std;

/*
Enter code for class Student here.
Read statement for specification.
*/
class Student{
    private: 
        int age, std;
        string fname, lname;
    public:
        void set_age(int a){
            //int age;
            age = a;
        }
        int get_age(){
            return age;
        }
        void set_first_name(string fn){
            //char fname[20];
            fname = fn;
        }
        string get_first_name(){
            return fname;
        }
        void set_last_name(string ln){
            //char fname[20];
            lname = ln;
        }
        string get_last_name(){
            return lname;
        }
        void set_standard(int s){
            //char fname[20];
            std = s;
        }
        int get_standard(){
            return std;
        }
        string to_string() 
            {
                stringstream ss;
                ss << age << "," << fname << "," << lname << "," << std;
                return ss.str();
            }
    
};

int main() {
    int age, standard;
    string first_name, last_name;
    
    cin >> age >> first_name >> last_name >> standard;
    
    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    
    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();
    
    return 0;
}
