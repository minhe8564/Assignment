#include <iostream>
#include <fstream>
#include <vector>
#include <climits>
using namespace std;

class SegmentTree {
private:
    vector<int> segTree;
    int n;

    void buildTree(vector<int>& A, int node, int start, int end) {
        if (start == end) {
            segTree[node] = start; 
        }
        else {
            int mid = (start + end) / 2;
            buildTree(A, 2 * node + 1, start, mid);
            buildTree(A, 2 * node + 2, mid + 1, end);
            segTree[node] = (A[segTree[2 * node + 1]] <= A[segTree[2 * node + 2]]) ? segTree[2 * node + 1] : segTree[2 * node + 2];
        }
    }

    int query(vector<int>& A, int node, int start, int end, int l, int r) {
        if (r < start || l > end) return -1; 
        if (l <= start && end <= r) return segTree[node];
        int mid = (start + end) / 2;
        int p1 = query(A, 2 * node + 1, start, mid, l, r);
        int p2 = query(A, 2 * node + 2, mid + 1, end, l, r);
        if (p1 == -1) return p2;
        if (p2 == -1) return p1;
        return (A[p1] <= A[p2]) ? p1 : p2;
    }

    void update(vector<int>& A, int node, int start, int end, int idx, int val) {
        if (start == end) {
            A[idx] = val;
        }
        else {
            int mid = (start + end) / 2;
            if (start <= idx && idx <= mid) {
                update(A, 2 * node + 1, start, mid, idx, val);
            }
            else {
                update(A, 2 * node + 2, mid + 1, end, idx, val);
            }
            segTree[node] = (A[segTree[2 * node + 1]] <= A[segTree[2 * node + 2]]) ? segTree[2 * node + 1] : segTree[2 * node + 2];
        }
    }

public:
    SegmentTree(vector<int>& A) {
        n = A.size();
        segTree.assign(4 * n, 0);
        buildTree(A, 0, 0, n - 1);
    }

    int query(vector<int>& A, int l, int r) {
        return query(A, 0, 0, n - 1, l, r);
    }

    void update(vector<int>& A, int idx, int val) {
        update(A, 0, 0, n - 1, idx, val);
    }
};

int main() {
    ifstream fin("rmq.inp");
    ofstream fout("rmq.out");

    int n;
    fin >> n;
    vector<int> A(n);

    for (int i = 0; i < n; i++) {
        fin >> A[i];
    }

    SegmentTree st(A);

    long sum = 0;
    int l, r, id, v;
    char command;

    while (fin >> command && command != 's') {
        switch (command) {
        case 'q': {
            fin >> l >> r;
            int minIdx = st.query(A, l, r);
            if (minIdx != -1) {
                sum += minIdx;
            }
            break;
        }
        case 'c': {
            fin >> id >> v;
            st.update(A, id, v);
            break;
        }
        }
    }

    fout << sum % 100000;
    cout << sum % 100000;

    fin.close();
    fout.close();

    return 0;
}
