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

/*
运用哈希表，对于每一个节点，查找哈希表中有没有k-root->val,如果有则说明搜索树中存在两个节点和为k
*/
class Solution {
public:
	unordered_set<int> hash_table;
	bool findTarget(TreeNode* root, int k) {
		if (root == nullptr)  //c++中空指针用nullptr表示
		{
			return false;
		}
		//if (hash_table.find(k - root->val) != hash_table.end())
		if (hash_table.count(k - root->val))
		{
			return true;
		}
		hash_table.insert(root->val);
		return findTarget(root->left, k) || findTarget(root->right, k);

	}
};

int main() {
	vector<int> root_num = { 5, 3, 6, 2, 4, NULL, 7 };
	TreeNode* root = createTree(root_num, 0);
	Solution s;
	cout << s.findTarget(root, 5) << endl;
	system("pause");
	return 0;
}
