#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream fin("rangeSum.inp");
	ofstream fout("rangeSum.out");

	long A[1000000];
	int n;
	fin >> n;

	for (int i = 0; i < n; i++) {
		fin >> A[i];
	}

	char command;
	while (fin >> command && command != 'q') {
		long a, b;
		long sum = 0;
		switch (command) {
			case 'c':
				fin >> a >> b;
				A[a-1] = b;
				break;
			case 's':
				fin >> a >> b;
				for (int i = a-1; i < b; i++) {
					sum += A[i];
				}
				fout << sum << '\n';
				break;
			default:
				break;
		}
	}

	fin.close();
	fout.close();

	return 0;
}
