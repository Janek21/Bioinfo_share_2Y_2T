
#include <iostream>
#include "Stack.hh"
using namespace std;

int main() {
  Stack<int> st;
  cout << "Just created a stack of height " << st.height() << endl;
  cout << "Now we will fill it in; please give me some integers" << endl;
  int n;
  while (cin >> n) st.push(n); 
  cout << "The stack has now height " << st.height() << endl;
  cout << "Now the integers will come out of the stack in reverse order, of course:" << endl;
  while (not st.is_empty()) {
	cout << st.top() << endl;
	st.pop();
  }
}
    
