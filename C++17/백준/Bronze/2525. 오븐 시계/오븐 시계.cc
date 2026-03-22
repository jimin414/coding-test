#include <iostream>
using namespace std;

int main() {
    int H, M, T;
    cin >> H >> M >> T;

    M += T;         
    H += M / 60;     
    M %= 60;         
    H %= 24;         

    cout << H << " " << M;
    return 0;
}