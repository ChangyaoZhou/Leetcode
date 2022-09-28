#include<string>
#include<unordered_set>
#include<iostream>
#include<vector>
using namespace std;

struct TreeNode {
	int val;
	TreeNode* left;
	TreeNode* right;
	TreeNode() : val(0), left(nullptr), right(nullptr) {}
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
	TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {} 
};


//构建二叉树
TreeNode* createTree(std::vector<int> nums, int i) {
	if (i >= nums.size() || nums[i] == NULL)               /**<出现无效下标 或者值为1均返回nullptr */
		return nullptr;

	TreeNode* root = new TreeNode(nums[i]);             /**<创建根节点 */
	root->left = createTree(nums, 2 * i + 1);                /**<创建左子树 */
	root->right = createTree(nums, 2 * i + 2);               /**<创建右子树 */

	return root;
}


class Solution {
public:
	int res = 0;
	int longestUnivaluePath(TreeNode* root) {
		dfs(root);
		return res; 
	}

	int dfs(TreeNode* root) { 
		if (root == nullptr) {
			return 0;
		}
		int left_len = 0;
		int right_len = 0;
		//left和right表示从当前节点的左右节点开始的有相同值的路径长度
		int left = dfs(root->left);
		int right = dfs(root->right);
		//left_len, right_len表示从当前节点开始，有相同值的路径长度
		//如果当前节点的值和左右节点的值相等，则在前面的left，right基础上加1
		if (root->left && root->val == root->left->val)
		{
			left_len = left + 1;
		}
		if (root->right && root->val == root->right->val)
		{
			right_len = right + 1;
		}
		//这里主要考虑的是同一个节点和他的左右节点都是同一个值，所以在同值的路径上会存在同一层的多个节点，所以要计算left_len + right_len
		//每一层时更新一次res，即最大同值路径长度，left_len + right_len可以包含路径上会存在同一层的多个节点，或者路径是从上到下的这两种情况
		res = max(res, left_len + right_len);  
		//如果同值路径包含上层节点和本层的多个节点，即路径上有分叉，只考虑其中一个分叉，所以只返回left_len, right_len中的较大值到上一层
		return max(left_len, right_len); 
		 
	}
};

int main() {
	vector<int> nodes = { 5, 4, 5, 1, 1, NULL, 5 };
	TreeNode* root = createTree(nodes, 0);
	Solution s;
	cout << s.longestUnivaluePath(root) << endl;
	system("pause");
	return 0;
}