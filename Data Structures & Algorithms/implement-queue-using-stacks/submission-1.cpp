class MyQueue {
public:
    stack<int> left, right;
    MyQueue() {}
    
    void push(int x) {
        left.push(x);
    }
    
    int pop() {
        if(right.empty()) loadRight();

        int val = right.top();
        right.pop();
        return val;
    }
    
    int peek() {
        if(right.empty()) loadRight();
        return right.top();
    }
    
    bool empty() {
        return right.empty() && left.empty();
    }

private:
    void loadRight(){
        while(!left.empty()){
            right.push(left.top());
            left.pop();
        }
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */