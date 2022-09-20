#include<string>
#include<stack>
#include<iostream>
using namespace std;

/*
和20题差不多，将字母依次放入栈，如果当前放入的字母和栈顶的字母相同，则说明是相邻重复的，或删去后是相邻重复的，
最后栈中剩下的字母，从栈底到栈顶的顺序排列，就是剩余的字符串
*/

string removeDuplicates(string s) {
	stack<char> st;
	//st.push(s[0]);
	for (int i = 0; i < s.size(); i++)
	{
		 
		if (st.empty() || s[i] != st.top())
		{
			
			st.push(s[i]); 
		}
		else
		{
			st.pop();
		}
	}
	if (st.empty())
	{
		return "";
	}
	string res;
	while (!st.empty())
	{
		res = st.top() + res;
		st.pop();
	}
	return res;	                     
}
int main() {
	string s = "abbaca";
	cout << removeDuplicates(s) << endl;
	system("pause");
	return 0;
} 

