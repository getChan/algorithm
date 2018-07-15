#include <iostream>

using namespace std;
static int comb[1001][1001];
int main(){
    
    int n, k;
    cin >> n >> k;
    
    for(int i=0; i<=n; i++){
        for(int j=0; j<=i; j++){
            if(j==0 || j==i)
                comb[i][j] = 1;
            else{
                comb[i][j] = comb[i-1][j-1] + comb[i-1][j];
            }
            comb[i][j] %= 10007;
        }
    }

    cout<< comb[n][k];

    return 0;
}