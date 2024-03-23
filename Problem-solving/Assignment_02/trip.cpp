#include <iostream>
#include <algorithm>
#include <fstream>
#include <cmath>
#include <iomanip>

using namespace std;

double money[1000];
double totalHigh = 0.0;
double totalLow = 0.0;

double sum(int n) {
	double total = 0;
	for (int i = 0; i < n; i++) {
		total += money[i];
	}
	return total;
}

int main() {
	int n;
	ifstream fin("trip.inp");
	ofstream fout("trip.out");
	while (fin >> n && n != 0) {
		for (int i = 0; i < n; i++) {
			fin >> money[i];
		}

		double avg = sum(n) / n;

		for (int i = 0; i < n; i++) {
			double total = money[i] - avg;
			if (total >= 0)
				totalHigh += floor(total * 100) / 100;
			else
				totalLow -= ceil(total * 100) / 100;
		}

		fout << fixed << setprecision(2) << "$" << max(totalHigh, totalLow) << endl;
		totalHigh = 0;
		totalLow = 0;
	}
	fin.close();
	fout.close();

	return 0;
}
