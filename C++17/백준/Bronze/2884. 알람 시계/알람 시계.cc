#include <iostream>
using namespace std;

int main() {
    int H, M;
    cin >>H>>M;

    if (M >= 45) {
        cout << H << " " << M - 45;
    } else {
        H = (H == 0) ? 23 : H - 1;
        cout << H << " " << M + 60 - 45;
    }

    return 0;
}