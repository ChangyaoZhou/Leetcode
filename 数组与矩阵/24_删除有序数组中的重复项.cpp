#include<string>
#include<unordered_set>
#include<iostream>
#include<vector>
using namespace std;

/*
从前向后遍历，如果出现和前面不同的数字，就把当前数字存下来
*/
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int curr_pos = 1;
        int num_pos = 1;
        while (curr_pos != nums.size())
        {
            if (nums[curr_pos] != nums[curr_pos - 1])
            {
                nums[num_pos] = nums[curr_pos];
                num_pos += 1;
            }
            curr_pos += 1; 

        }
        return num_pos;
    }
};

int main() {
    //vector<int> nums = { 0, 0, 1, 1, 1, 2, 2, 3, 3, 4 };
    vector<int> nums = {1, 1, 2};
    Solution s;
    cout << s.removeDuplicates(nums) << endl;
    system("pause");
    return 0;
}