#include<vector>
#include<iostream>
using namespace std;

struct ListNode {
	int val;
	ListNode* next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode* next) : val(x), next(next) {}
};

struct TreeNode {
	int val;
	TreeNode* left;
	TreeNode* right;
	TreeNode() : val(0), left(nullptr), right(nullptr) {}
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
	TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};

ListNode* create_node_list(vector<int> node_val) {
	ListNode* head = new ListNode(node_val[0]);
	ListNode* curr_node = head;
	for (int i = 1; i < node_val.size(); i++) {
		ListNode* node = new ListNode(node_val[i]); 
		curr_node->next = node;
		curr_node = curr_node->next;
	}
	return head;
}

void print_node_list(ListNode* root) {
	while (root != nullptr) {
		cout << root->val << endl;
		root = root->next;
	}
	return;
}


class Solution {
public:
	ListNode* get_median(ListNode* head) { 
		ListNode* slow = head;
		ListNode* fast = head;
		while (fast->next != nullptr && fast != nullptr) {
			slow = slow->next;
			fast = fast->next->next;
		}
		return slow;
	}
	TreeNode* sortedListToBST(ListNode* head) {
		if (head == nullptr)
		{
			return nullptr;
		}
		
		ListNode* mid_node = get_median(head); 
		TreeNode* root = new TreeNode(mid_node->val); 
		mid_node->next = nullptr;
		root->left = sortedListToBST(head);
		root->right = sortedListToBST(mid_node->next);
		return root;
		} 
};

int main() {
	vector<int> nodes = { -10,-3,0,5,9 };
	ListNode* head = create_node_list(nodes);
	print_node_list(head);
	Solution s;
	TreeNode* root = s.sortedListToBST(head);
	cout << "print result: " << endl;
	
	system("pause");
	return 0;
}

