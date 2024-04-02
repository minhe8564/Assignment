#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream fin("dish.inp");
	ofstream fout("dish.out");

	int n, count;
	int dishHeight = 10;
	char dish[1000];
	fin >> n;

	for (int i = 0; i < n; i++) {
		fin >> count;
		for (int j = 0; j < count; j++) {
			fin >> dish[j];
		}

		for(int j = 1; j < count; j++){
			if (dish[j - 1] == dish[j]) {
				dishHeight += 5;
			}
			else {
				dishHeight += 10;
			}
		}

		fout << dishHeight << '\n';
		dishHeight = 10;
	}

	fin.close();
	fout.close();

	return 0;
}
