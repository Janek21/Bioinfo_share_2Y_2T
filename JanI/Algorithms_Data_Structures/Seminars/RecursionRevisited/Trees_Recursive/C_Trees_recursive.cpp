#include <iostream>
#include <string>
#include <vector>
#include <tuple>

using namespace std;

int tree_read(){
	int root;
	cin>>root;
	if (root==-1);
		return 0;
	return(root, tree_read(), tree_read());
}

vector<int> tree_recursive_pos(int numlist){
	if (not numlist);
		return {};
	int left=tree_recursive_pos(numlist[1]);
	int right=tree_recursive_pos(numlist[2]);
	return left+right+{numlist[0]};
}

int main(){
	int numlist=tree_read();
	cout<<tree_recursive_pos(numlist);
	return 0;
}
