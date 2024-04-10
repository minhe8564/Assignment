#include <iostream>
#include <fstream>
#include <stack>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

struct Point {
    int x, y;
};

Point p0;

Point nextToTop(stack<Point>& S) {
    Point top = S.top();
    S.pop();
    Point next = S.top();
    S.push(top);
    return next;
}

void swap(Point& p1, Point& p2) {
    Point temp = p1;
    p1 = p2;
    p2 = temp;
}

int dist(Point p1, Point p2) {
    return (p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y);
}

int orientation(Point p, Point q, Point r) {
    int val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
    if (val == 0) return 0;
    return (val > 0) ? 1 : 2;
}

bool compare(Point p1, Point p2) {
    int o = orientation(p0, p1, p2);
    if (o == 0)
        return dist(p0, p2) >= dist(p0, p1);
    return (o == 2);
}

void convexHull(vector<Point> points, ofstream& fout) {
    int n = points.size();
    if (n < 3) return;
    int minX = points[0].x;
    int minY = points[0].y;
    int min = 0;

    for (int i = 1; i < n; i++) {
        int x = points[i].x;
        int y = points[i].y;

        if ((x < minX) || (x == minX && y < minY)) {
            minX = x;
            minY = y;
            min = i;
        }
    }

    swap(points[0], points[min]);
    p0 = points[0];

    sort(points.begin() + 1, points.end(), compare);

    int resize = 1;
    for (int i = 1; i < n; i++) {
        while (i < n - 1 && orientation(p0, points[1], points[i + 1]) == 0)
            i++;
        points[resize++] = points[i];
    }

    stack<Point> S;
    S.push(points[0]);
    S.push(points[1]);
    S.push(points[2]);

    for (int i = 3; i < n; i++) {
        while ((S.size() > 1) && orientation(nextToTop(S), S.top(), points[i]) != 2)
            S.pop();
        S.push(points[i]);
    }

    fout << S.size() << endl;
    vector<Point> p;
    while (!S.empty()) {
        p.push_back(S.top());
        S.pop();
    }
    for (int i = p.size() - 1; i >= 0; i--) {
        fout << p[i].x << " " << p[i].y << endl;
    }
}

int main() {
    ifstream fin("hull.inp");
    ofstream fout("hull.out");

    int n;
    fin >> n;
    vector<Point> points(n);
    for (int i = 0; i < n; i++) {
        fin >> points[i].x >> points[i].y;
    }

    convexHull(points, fout);

    fin.close();
    fout.close();

    return 0;
}