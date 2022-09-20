#include<vector>
#include<queue>
#include<iostream>
using namespace std;


class MyStack {
public:
    //queue不能遍历，只能通过top()，back()访问，通过pop,push增减元素
    queue<int> que_in;
    queue<int> que_cache;
    MyStack() {
    }

    void push(int x) {
        que_in.push(x);
    }

    /*
    int pop() {
        //que2其实完全就是一个备份的作用
        //把que1最后面的元素以外的元素都备份到que2，然后弹出最后面的元素，再把其他元素从que2导回que1。
        while (que_in.size() != 1)
        {
            que_cache.push(que_in.front());
            que_in.pop();
        }
        int result = que_in.front();
        que_in.pop();
        
        //此时que_in已经为空，将que_cache完全复制给que_in，然后再清空que_cache
        que_in = que_cache;
        while (!que_cache.empty())
        {
            que_cache.pop();
        }
        return result;
    }
    */

    int pop() {
        //优化的方法：只用一个队列就够了
        //一个队列在模拟栈弹出元素的时候只要将队列头部的元素（除了最后一个元素外） 
        //重新添加到队列尾部，此时在去弹出元素就是栈的顺序了
        int size = que_in.size();
        size--;
        while (size--) { // 将队列头部的元素（除了最后一个元素外） 重新添加到队列尾部
            que_in.push(que_in.front());
            que_in.pop();
        }
        int result = que_in.front(); // 此时弹出的元素顺序就是栈的顺序了
        que_in.pop();
        return result;
    }

    int top() {
        return que_in.back();
    }

    bool empty() {
        return que_in.empty();
    }
};
