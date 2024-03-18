#include <iostream>
using namespace std;

int main() {
    int x = 5;
    int *p, *q, *r;
    p = &x;
    x = 5;
    q = NULL;
    q = p;
    r = new int;
    *r = 85;
    cout << r << " " << *r << endl;
}
