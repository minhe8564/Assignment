#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

bool isJollyJumper(vector<int>& num) {
	int n = num.size();
	vector<bool> diffs(n - 1, false);

	for (int i = 1; i < n; i++) {
		int diff = abs(num[i] - num[i - 1]);
		if (diff < 1 || diff >= n || diffs[diff - 1])
			return false;
		
		diffs[diff - 1] = true;

		if (i == n - 1)
			return true;
	}
	return true;
}

int main() {
	ifstream fin("jolly.inp");
	ofstream fout("jolly.out");

	int n;
	while (fin >> n) {
		vector<int> num(n);
		for (int i = 0; i < n; i++) {
			fin >> num[i];
		}

		if (isJollyJumper(num))
			fout << "Jolly" << endl;
		else
			fout << "Not Jolly" << endl;
	}

	fin.close();
	fout.close();

	return 0;
}