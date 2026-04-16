class Solution {
public:
    vector<string> rslt;

    void generateString(int openCount, int closeCount, int notClosed, string cur){
        if(openCount < 0 || closeCount < 0) return;
        if(closeCount == 0 && openCount > 0) return;

        if(openCount == 0 && closeCount == 0){
            if(notClosed == 0) rslt.push_back(cur);
            return;
        }

        if(notClosed > 0){
            cur.append(")");
            generateString(openCount, closeCount-1, notClosed-1, cur);
            cur.pop_back();
        }

        cur.append("(");
        generateString(openCount-1, closeCount, notClosed+1, cur);
        cur.pop_back();
    }

    vector<string> generateParenthesis(int n) {
        generateString(n-1, n, 1, "(");
        return rslt;
    }
};
