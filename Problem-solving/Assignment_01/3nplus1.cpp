#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

int cycleLength(int n) {
    int length = 1;
    while (n != 1) {
        if (n % 2 == 1)
            n = 3 * n + 1;
        else
            n = n / 2;
        length++;
    }
    return length;
}

int main() {
    ifstream fin("3nplus1.inp");
    ofstream fout("3nplus1.out");

    int i, j;
    while (fin >> i >> j) {
        int maxLength = 0;
        for (int n = min(i, j); n <= max(i, j); n++) {
            int currentLength = cycleLength(n);
            maxLength = max(maxLength, currentLength);
        }
        fout << i << " " << j << " " << maxLength << endl;
    }

    fin.close();
    fout.close();

    return 0;
}
