#include <iostream>
using namespace std;

int main(){
    int l,a,b,c,d;
    cin >> l;
    cin >> a;
    cin >> b;
    cin >> c;
    cin >> d;

    int day = 0;

    while(l>0){
        if(a<=0 && b<=0)
            day++;
        a -=c;
        b -=d;
        l--;
    }
    cout << day;
    return 0;
}