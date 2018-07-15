#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    char *seat = new char[n+1];
    cin >> seat;
    int cupholder = 1;

    int i = 0;
    while(i<n){
        if(seat[i] == 'S'){
            i++;
        }
        else{
            i += 2;
        }
        cupholder++;
        
    }
    if(cupholder>n)
        cout << n;
    else
        cout << cupholder;
    return 0;
}