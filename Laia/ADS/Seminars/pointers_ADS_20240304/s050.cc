#include <iostream>
using namespace std;

struct Node {
  int data;
  Node *next;
};

int traverse_sum_it(Node *head) {
	int s = 0;
	Node *m = head;
	while (m != NULL) {
		s += m->data;
		m = m->next;
	}
	return s;
}

int traverse_sum(Node *head) {
	if (head == NULL) return 0;
	else return head->data + traverse_sum(head->next);
}

int main ( ) {
	Node *head = NULL;
	for (int i=1;i<10;++i) {
		Node *n = new Node;
		n->data = i;
		n->next = head;
		head = n;
	}
	cout << traverse_sum(head) << endl;
}
