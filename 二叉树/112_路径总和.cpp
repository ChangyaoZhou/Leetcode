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
注意 问的是是否存在从当前节点 root 到叶子节点的路径！
如果只有根节点一个节点，或者是中间一段路径，没有达到最下层的叶子节点，还是要返回false。
所以当且仅当 当前节点是一个叶子节点，即root->left == nullptr && root->right == nullptr，才判断对应的路径上节点加和是否为target
而不是在遍历每一层的节点都比较路径和与target是否相等
*/
class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
		if (root == nullptr)
		{
			return false;
		}
		if (root->left == nullptr && root->right == nullptr)
		{
			return targetSum == root->val;
		} 
		bool if_left = hasPathSum(root->left, targetSum - root->val);   
		bool if_right = hasPathSum(root->right, targetSum - root->val);  
		return 	if_left || if_right;
		
    }
};

int main() {
	vector<int> nodes = { 1, 2 };
	int targetSum = 1;
	TreeNode* root = createTree(nodes, 0);
	Solution s;
	cout << s.hasPathSum(root, 22) << endl;
	system("pause");
	return 0;
}
	
