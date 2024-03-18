
#include "Stack.hh"
// using namespace std;

int main() {
  Stack<int> st;
  int z = 0;
  st.push(3);
  st.push(2); 
  if (st.top() != 2) z = 1/z;
  st.pop();
  if (st.top() != 3) z = 1/z;
  st.pop();
  if (not st.is_empty()) z = 1/z;
}
    
