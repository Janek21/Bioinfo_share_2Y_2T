#include <iostream>
using namespace std;

int main() {
  int x;
  int* p;
  p = &x;
  x = 5;
  cout << *p << endl;  // writes 5
  *p = 3;
  cout << x << endl;   // writes 3
}
