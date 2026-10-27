class MinStack {

private:
    vector<vector<int>> stack;
public:
    MinStack() {
    }
    
    void push(int val) {
        int min_val = getMin();
        if(stack.empty() || val<min_val) min_val = val;
        stack.push_back({val,min_val});    
    }
    
    void pop() {
        return stack.pop_back();
    }
    
    int top() {
        if(stack.empty()) return -1;
        else return stack.back()[0];
    }
    
    int getMin() {
        if(stack.empty()) return -1;
        else return stack.back()[1];
    }
};