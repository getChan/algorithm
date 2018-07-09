#include <iostream>
#include <list>
#include <algorithm>
#include <cstring>
using namespace std;

typedef struct dirtype{
    int dirsec;
    char ld;
}dirtype;

typedef struct zmijatype{
    int row;
    int col;
}zmijatype;

int main(){
    int n, k, l;

    cin >> n;
    cin >> k;
    int **map = new int*[n+1];
    for(int i = 0; i < n+1; i++) {
        map[i] = new int[n+1];
        memset(map[i], 0, sizeof(int)*(n+1)); // 메모리 공간을 0으로 초기화
    }

    int applerow, applecol;
    const int APPLEPOINT = 2;   // 사과 위치
    for(int i=0; i<k; i++){
        cin >> applerow >> applecol;
        map[applerow-1][applecol-1] = APPLEPOINT;
    }
    cin >> l;
    dirtype dir[l];
    for(int i=0; i<l; i++){
        cin >> dir[i].dirsec >> dir[i].ld;
    }

    list<zmijatype> zmija;
    zmija.push_front({0, 0});

    char headdir = 'R'; //뱀대가리 방향
    
    int sec = 0;
    int diri = 0;
    int flag = -1;
    while((zmija.front().row<n)&&(zmija.front().col<n)&&(zmija.front().row>=0)&&(zmija.front().col>=0)&&(flag!=1)){
        sec++;
        switch (headdir) //방향에 따라 진행
        {
            case 'R':
                zmija.push_front({zmija.front().row, zmija.front().col+1});
                break;
                
            case 'D':
                zmija.push_front({zmija.front().row+1, zmija.front().col});
                break;

            case 'L':
                zmija.push_front({zmija.front().row, zmija.front().col-1});
                break;

            case 'U':
                zmija.push_front({zmija.front().row-1, zmija.front().col});
                break;
            default:
                std::cout << "뱀 진행 오류";
                break;
        }
        if(zmija.front().row<0 || zmija.front().col<0){ //인덱스 오류 처리
            zmija.front() = {n, n};
        }

        list<zmijatype>::iterator itor; //  뱀과 부딪히는지 판별
        int cnt = 0;
        for(itor=zmija.begin(); itor!=zmija.end(); itor++){
            if(itor->row == zmija.front().row && itor->col == zmija.front().col)
                cnt++;
        }
        if(cnt>1)
            flag = 1;

        if(map[zmija.front().row][zmija.front().col] != APPLEPOINT){    // 사과가 없으면
            zmija.pop_back();
        }
        else{
            map[zmija.front().row][zmija.front().col] = 0;
        }

        if(sec == dir[diri].dirsec){    // 방향 바뀌는 시간 되면
            if(headdir == 'R'){ // 오른쪽 진행 중
                if(dir[diri].ld == 'L')
                    headdir = 'U';
                else if(dir[diri].ld == 'D')
                    headdir = 'D';
            }
            else if (headdir == 'D'){   // 아래방향 진행 중
                if(dir[diri].ld == 'L')
                    headdir = 'R';
                else if(dir[diri].ld == 'D')
                    headdir = 'L';
            }
            else if (headdir == 'L'){   // 왼쪽방향 진행 중
                if(dir[diri].ld == 'L')
                    headdir = 'D';
                else if(dir[diri].ld == 'D')
                    headdir = 'U';
            }
            else{   // 위쪽방향 진행 중
                if(dir[diri].ld == 'L')
                    headdir = 'L';
                else if(dir[diri].ld == 'D')
                    headdir = 'R';
            }
            diri++;
        }
        if(flag == 1)
            break;
    }
    cout << sec;
    return 0;
}