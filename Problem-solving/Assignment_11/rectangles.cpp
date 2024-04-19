#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int findMaxRectangles(int wireLength) {
    vector<pair<int, int>> rectangles;

    for (int m = 2; ; m++) {
        bool found = false;
        for (int n = 1; n < m; n++) {
            if ((m - n) % 2 == 1 && gcd(m, n) == 1) {
                int a = m * m - n * n;
                int b = 2 * m * n;
                if (2 * (a + b) > wireLength) break;
                rectangles.push_back({ a, b });
                found = true;
            }
        }
        if (!found) break;
    }

    sort(rectangles.begin(), rectangles.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
        return 2 * (a.first + a.second) < 2 * (b.first + b.second);
    });

    int count = 0;
    int usedLength = 0;
    for (auto& rect : rectangles) {
        int perimeter = 2 * (rect.first + rect.second);
        if (usedLength + perimeter <= wireLength) {
            usedLength += perimeter;
            count++;
        }
        else {
            break;
        }
    }

    return count;
}

int main() {
    ifstream fin("rectangles.inp");
    ofstream fout("rectangles.out");

    int testCases, wireLength;
    fin >> testCases;

    while (testCases--) {
        fin >> wireLength;
        fout << findMaxRectangles(wireLength) << endl;
    }

    fin.close();
    fout.close();

    return 0;
}
