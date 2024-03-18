
#include <iostream>
#include "Queue.hh"
using namespace std;

int main() {
  Queue<int> queue;
  cout << "Just created a queue of length " << queue.length() << endl;
  cout << "Now we will fill it in; please give me some integers" << endl;
  int n;
  while (cin >> n) queue.push_back(n); 
  cout << "The queue has now length " << queue.length() << endl;
  cout << "Now the integers will come out of the queue in the same order, of course:" << endl;
  while (not queue.is_empty()) {
	cout << queue.front() << endl;
	queue.pop_front();
  }
}
    
