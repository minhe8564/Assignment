#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int sum;
int* cycleArray;
int* tempArray;

void nextCycle(int index) {
	tempArray[index] = 1;
	if (tempArray[cycleArray[index]] == 1)
		sum++;
	else
		nextCycle(cycleArray[index]);
}

int main() {
	ifstream fin("cycle.inp");
	ofstream fout("cycle.out");

	int n;
	fin >> n;

	while (n--) {
		int arrIndex = 0;
		fin >> arrIndex;
		
		cycleArray = new int[arrIndex];
		tempArray = new int[arrIndex];

		for (int i = 0; i < arrIndex; i++) {
			fin >> cycleArray[i];
			tempArray[i] = 0;
			cycleArray[i]--;
		}

		for (int i = 0; i < arrIndex; i++) {
			if (tempArray[i] == 0) {
				nextCycle(i);
			}
		}

		fout << sum << endl;
		sum = 0;
	}

	fin.close();
	fout.close();

	return 0;
}