#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> p(n);
    for (int i = 0; i < n; ++i) {
        cin >> p[i];
    }
    prev_permutation(begin(p), end(p));
    for (int i = 0; i < n; ++i) {
        cout << p[i] << " \n"[i + 1 == n];
    }
    return 0;
}