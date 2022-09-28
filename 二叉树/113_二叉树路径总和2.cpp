#include<vector>
#include<iostream>
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

/*
类似112题，每当遍历到最下一层的叶子节点时，比较当前的路径和与target是否相等，如果相等就把路径存到result中，
注意 返回上一层时，要把path中的最后一位去掉，回溯时需要恢复到上一层的状态
*/

class Solution {
public:
	vector<vector<int>> result;
	vector<int> path;
	vector<vector<int>> pathSum(TreeNode* root, int targetSum) { 
		dfs(root, targetSum);
		return result;  
	}

	void dfs(TreeNode* root, int target) {
		if (root == nullptr)
		{
			return;
		}
		path.push_back(root->val);
		if (root->left == nullptr && root->right == nullptr) 
		{
			if (target == root->val) {
				result.push_back(path);
			}
			return;
		}

		if (root->left != nullptr) {
			dfs(root->left, target - root->val);
			path.pop_back();
		}

		if (root->right != nullptr) {
			dfs(root->right, target - root->val);
			path.pop_back();
		}
	}
};

int main() {
	vector<int> nodes = { 5, 4, 8, 11, NULL, 13, 4, 7, 2, NULL, NULL, 5, 1 };
	int targetSum = 22; 
	TreeNode* root = createTree(nodes, 0);
	Solution s;
	vector<vector<int>> result = s.pathSum(root, 22); 
	system("pause");
	return 0;
}