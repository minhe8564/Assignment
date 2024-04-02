#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

const int MOD = 1000000007;

int main() {
    ifstream fin("grid.inp");
    ofstream fout("grid.out");

    int n;
    fin >> n;

    for (int i = 0; i < n; i++) {
        int x, y, a, b, k;
        fin >> x >> y >> a >> b >> k;

        vector<vector<bool>> points(x + 1, vector<bool>(y + 1, false));
        vector<vector<bool>> obstacles(x + 1, vector<bool>(y + 1, false));
        vector<vector<vector<int>>> countPaths(x + 1, vector<vector<int>>(y + 1, vector<int>(k + 1, 0)));

        for (int i = 0; i < a; i++) {
            int px, py;
            fin >> px >> py;
            points[px][py] = true;
        }

        for (int i = 0; i < b; i++) {
            int ox, oy;
            fin >> ox >> oy;
            obstacles[ox][oy] = true;
        }

        countPaths[0][0][0] = 1;
        for (int i = 1; i <= x; i++) {
            if (!obstacles[i][0]) {
                if (points[i][0]) {
                    for (int j = 1; j <= k; j++)
                        countPaths[i][0][j] = countPaths[i - 1][0][j - 1];
                    countPaths[i][0][k] += countPaths[i - 1][0][k];
                }
                else {
                    for (int j = 0; j <= k; j++)
                        countPaths[i][0][j] = countPaths[i - 1][0][j];
                }
            }
            else {
                break;
            }
        }

        for (int i = 1; i <= y; i++) {
            if (!obstacles[0][i]) {
                if (points[0][i]) {
                    for (int j = 1; j <= k; j++)
                        countPaths[0][i][j] = countPaths[0][i - 1][j - 1];
                    countPaths[0][i][k] += countPaths[0][i - 1][k];
                }
                else {
                    for (int j = 0; j <= k; j++)
                        countPaths[0][i][j] = countPaths[0][i - 1][j];
                }
            }
            else {
                break;
            }
        }

        for (int i = 1; i <= x; i++) {
            for (int j = 1; j <= y; j++) {
                if (!obstacles[i][j]) {
                    if (points[i][j]) {
                        for (int point = 1; point <= k; point++)
                            countPaths[i][j][point] = (countPaths[i - 1][j][point - 1]
                                + countPaths[i][j - 1][point - 1]) % MOD;
                        countPaths[i][j][k] = (countPaths[i][j][k] + (countPaths[i - 1][j][k]
                            + (countPaths[i][j - 1][k])) % MOD) % MOD;
                    }
                    else {
                        for (int point = 0; point <= k; point++)
                            countPaths[i][j][point] = (countPaths[i - 1][j][point]
                                + countPaths[i][j - 1][point]) % MOD;
                    }
                }
            }
        }

        fout << countPaths[x][y][k] << '\n';
    }
    fin.close();
    fout.close();

    return 0;
}
