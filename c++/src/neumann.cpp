#include <iostream>
#include <string>
using namespace std;
int main() {
	int s, t, d;
	cin >> s >> t >> d;
    int rst = d / (2 * s) * t;
	cout << rst << endl;
	return 0;
}