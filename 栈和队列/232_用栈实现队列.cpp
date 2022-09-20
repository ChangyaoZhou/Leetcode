#include<vector>
#include<stack>
#include<iostream>
using namespace std;

class MyQueue {
public:
    //stack不能遍历，只能通过top()访问，通过pop,push增减元素
    //为了达到队列先进先出的效果，需要用两个栈st_in，st_out，两个栈中的所用元素加起来是当前队列中的所有元素
    //两个栈st_in，st_out没有公共的元素
    stack<int> st_in;
    stack<int> st_out;
    MyQueue() { 

    }

    /* Push element x to the back of queue. */
    void push(int x) {
        st_in.push(x);
    }
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        //从队列中移除队列时，优先从st_out中移除，如果st_out为空，需要将st_in中的元素移动到st_out中
        //e.g. 元素按1，2，3，4的顺序进入st_in栈，则按4，3，2，1的顺序出st_in栈
        //则按照4，3，2，1的顺序进入st_out栈，则按照1，2，3，4的顺序出st_out栈，正好可以实现队列的【先进先出】
        if (st_out.empty())
        {
            while (!st_in.empty())
            {
                st_out.push(st_in.top());
                st_in.pop();
            }
        }
        int result = st_out.top();
        st_out.pop();
        return result;
    }
    /* Get the front element.BUT don't remove the front element! */
    int peek() {
        int result = this->pop();
        st_out.push(result); //这里直接调用前面写好的pop函数，但是pop函数中将最顶上的元素移除了，所以要再加回去
        return result;
    }
    /* Returns whether the queue is empty. */
    bool empty() {
        //st_in，st_out，两个栈中的所用元素加起来是当前队列中的所有元素,只有两个栈都空了，该队列才是空的
        return st_in.empty() && st_out.empty();
    }
};