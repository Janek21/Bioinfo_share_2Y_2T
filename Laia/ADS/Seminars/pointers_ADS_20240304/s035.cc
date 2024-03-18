#include <iostream>
using namespace std;
int main ( ) {
  int *p ;
  if ( true ) {
    int x = 5;
    p = &x ;
  }
  cout << *p << endl ;
}
