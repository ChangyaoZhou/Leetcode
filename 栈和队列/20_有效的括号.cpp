#include<stack>
#include<string>
#include<iostream>
using namespace std;
/*
不匹配的三种情况
第一种情况，字符串里向左方向的括号多余了，e.g. {{[]}
第二种情况，括号没有多余，但是 括号的类型没有匹配上，e.g.{(]}
第三种情况，字符串里右方向的括号多余了，所以不匹配，e.g.{()}}

*/
bool isValid(string s) {
	//首先s长度一定要是偶数，才有可能是有效的
	if (s.size() % 2 == 1)
	{
		return false;
	}
	stack<char> st;
	for (int i = 0; i < s.size(); i++)
	{
		//如果是向左符号([{，则向栈中添加相反方向的向右括号，然后和s中后面的向右括号进行比较
		if (s[i] == '(')
		{
			st.push(')');
		}
		else if (s[i] == '[')
		{
			st.push(']');
		}
		else if (s[i] == '{')
		{
			st.push('}');
		}
		//对应第三种情况，栈中已经没有向左的括号对应当前的向右符号
		else if (st.empty())
		{
			return false;
		} 
		else if (s[i] == st.top())
		{
			st.pop();
		}
		//对应第二种情况，括号类型不对
		else
		{
			return false;
		}
		
	}
	//对应第一种情况，向左方向的括号多了，遍历完整个s，没有别的向右括号与之对应
	return st.empty();
}

int main() {
	string s = "([}}])";
	cout << isValid(s) << endl;
	system("pause");
	return 0;
} 

 