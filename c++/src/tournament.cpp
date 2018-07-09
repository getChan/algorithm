#include <iostream>
using namespace std;
int main(){
    int n, a, b;
    int cnt = 0;
    cin >> n >> a >> b;
    while(a != b){
        cnt++;
        a = (a+1)/2;
        b = (b+1)/2;
    }
    cout << cnt;
    return 0;
}