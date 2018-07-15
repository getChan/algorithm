#include <iostream>
#include <list>
using namespace std;

void rotate(list<int> gear){
    gear.push_front(gear.back());
    gear.pop_back();
}
void crotate(list<int> gear){
    gear.push_back(gear.front());
    gear.pop_front();
}
int main(){
    list<int> gear[4];
    char input[9];
    int three[4], nine[4];
    
    for(int i=0; i<4; i++){ //기어 초기화
        cin >> input;
        for(int j=0; j<8; j++){
            gear[i].push_front(input[j]-48);
        }
        three[i] = input[2]-48;
        nine[i] = input[6]-48;
    }
    int k;
    cin >> k;
    for(int i=0; i<k; i++){
        int gearnum = 0, direction = 0;
        cin >> gearnum >> direction;
        
        if(three[gearnum])
    }
    
    return 0;
}