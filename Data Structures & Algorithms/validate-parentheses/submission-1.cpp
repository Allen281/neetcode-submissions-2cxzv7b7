class Solution {
public:
    bool isValid(string s) {
        stack<char> open;

        for(char c : s){
            if(c == '(' || c == '{' || c == '[') open.push(c);

            else{
                if(open.empty()) return false;

                switch(c){
                    case ')':
                        if(open.top() != '(') return false;
                        else open.pop();
                        break;
                    case '}':
                        if(open.top() != '{') return false;
                        else open.pop();
                        break;
                    case ']':
                        if(open.top() != '[') return false;
                        else open.pop();
                        break;
                }
            }
        }

        return open.empty();
    }
};
