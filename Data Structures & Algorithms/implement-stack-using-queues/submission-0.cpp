class MyStack {
public:
    queue<int> left, right;
    MyStack() {}
    
    void push(int x) {
        right.push(x);

        while(!left.empty()){
            right.push(left.front());
            left.pop();
        }

        swap(left, right);
    }
    
    int pop() {
        int val = left.front();
        left.pop();
        return val;
    }
    
    int top() {
        return left.front();
    }
    
    bool empty() {
        return left.empty() && right.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */