#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
using namespace std;

struct Point {
	long x, y;
};

long distSquared(Point p1, Point p2) {
	long x = p2.x - p1.x;
	long y = p2.y - p1.y;
	return x * x + y * y;
}

bool isParallelogram(Point points[4]) {
	set<long> distSet;

	int k = 0;
	for (int i = 0; i < 4; i++) 
		for (int j = i + 1; j < 4; j++) 
			distSet.insert(distSquared(points[i], points[j]));
	return distSet.size() == 2 || distSet.size() == 4;
}

int main() {
	ifstream fin("parallelogram.inp");
	ofstream fout("parallelogram.out");

	Point points[4];
	while (fin >> points[0].x >> points[0].y >> points[1].x >> points[1].y
		>> points[2].x >> points[2].y >> points[3].x >> points[3].y) {
		if (points[0].x == 0 && points[0].y == 0 && points[1].x == 0 && points[1].y == 0 &&
			points[2].x == 0 && points[2].y == 0 && points[3].x == 0 && points[3].y == 0) break;

		if (isParallelogram(points))
			fout << 1 << endl;
		else
			fout << 0 << endl;

	}

	fin.close();
	fout.close();

	return 0;
}