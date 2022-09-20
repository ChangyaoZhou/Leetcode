#include<string>
#include<stack>
#include<iostream>
#include<vector>
using namespace std;

/*
逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。 
平常使用的算式则是一种中缀表达式，如 ( 1 + 2 ) * ( 3 + 4 ) 。
该算式的逆波兰表达式写法为 ( ( 1 2 + ) ( 3 4 + ) * ) 。 

所以可以将数字依次放入栈中，如果当前位置是运算符号，则从栈顶依次取出两个数字进行运算，再把运算结果放回栈顶
*** 注意运算的顺序  a，b，/  --> a / b
*/
int evalRPN(vector<string>& tokens) {
	stack<int> st;
	for (int i = 0; i < tokens.size(); i++)
	{
		if (tokens[i] == "+" || tokens[i] == "-" || tokens[i] == "*" || tokens[i] == "/")
		{
			//使用int类型会overflow
			long x = st.top();
			st.pop();
			long y = st.top();
			st.pop();
			if (tokens[i] == "+") st.push(y + x);
			if (tokens[i] == "-") st.push(y - x);
			if (tokens[i] == "*") st.push(y * x);
			if (tokens[i] == "/") st.push(y / x); 
			//cout << st.top() << endl; 
		}
		else
		{
			//stoi可将字符串转化为整数
			st.push(stoi(tokens[i]));
		}
	}
	return st.top();
}

int main() {
	vector<string> tokens = {"-128","-128","*","-128","*","-128","*","8","*","-1","*"};
	cout << evalRPN(tokens) << endl;
	system("pause");
	return 0;
}
