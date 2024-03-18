#include <iostream>
using namespace std;

struct Node {
  int data;
  Node *lst, *rst;
};

void insert(Node **rootref, int val) {
	if (*rootref == NULL) {
		Node *n = new Node;
		n->data = val;
		n->lst = NULL;
		n->rst = NULL;
		*rootref = n;
	}
	else if (val < (*rootref)->data) {
		insert(&(*rootref)->lst, val);
	}
	else if (val > (*rootref)->data) {
		insert(&(*rootref)->rst, val);
	}
};

void inorder_traversal(Node *t) {
	if (t != NULL) {
		inorder_traversal(t->lst);
		cout << t->data << endl;
		inorder_traversal(t->rst);
	}
}

int main ( ) {
	Node *t = NULL;
	int n;
	for (int i=0; i < 10; ++i) {
		cin >> n;
		insert(&t, n);
	}
	cout << "sorted:" << endl;
	inorder_traversal(t);
}
