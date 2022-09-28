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
暴力解法，用DFS遍历所有可能的路径，将所得到的路径字符串反转，然后更新出最小的字符串。
*/
class Solution {
public:
	string min_path = "zzz";
    string smallestFromLeaf(TreeNode* root) {
		if (root == nullptr) {
			return "";
		}
		string path;
		dfs(root, path);
		return min_path;

    }


	void dfs(TreeNode* root, string& path) {
		path.push_back('a' + root->val);
		if (root->left == nullptr && root->right == nullptr) {
			//这里reverse是将path进行原地反转，没有返回值，所以需要更新最小字符串之后再把字符串反转回来
			reverse(path.begin(),path.end());
			min_path = min(min_path, path);
			reverse(path.begin(), path.end());
			return;
		} 
		//每次回到上一层时，将path中最后一项移除，恢复到上一层的状态
		if (root->left != nullptr) {
			dfs(root->left, path);
			path.pop_back();
		}
		
		if (root->right != nullptr) {
			dfs(root->right, path);
			path.pop_back();
		} 
	}
};

int main() {
	vector<int> nodes = { 25,1,3,1,3,0,2 };
	TreeNode* root = createTree(nodes, 0);
	Solution s;
	string result = s.smallestFromLeaf(root);
	cout << "print result" << endl;
	cout << result << endl;
	system("pause");
	return 0;
}
