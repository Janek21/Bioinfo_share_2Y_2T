#include <iostream>
using namespace std;

typedef struct {
	int code;
	string name;
  } st;

int main() {
  st *p = new st;
  (*p).code = 9;
  (*p).name = "aeiou";
  cout << (*p).code << endl;
  cout << (*p).name << endl;
  cout << p->code << endl;
  cout << p->name << endl;

}
