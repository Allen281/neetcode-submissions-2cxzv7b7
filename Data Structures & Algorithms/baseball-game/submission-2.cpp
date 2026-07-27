class Solution {
public:
    int calPoints(vector<string>& operations) {
        stack<int> scores;
        int rslt = 0;

        for(string o : operations){
            if(o == "+"){
                int first = scores.top(); scores.pop();
                int second = scores.top(); scores.pop();
                rslt += first+second;
                scores.push(second);
                scores.push(first);
                scores.push(first+second);
            } else if(o == "D"){
                rslt += scores.top()*2;
                scores.push(scores.top()*2);
            } else if(o == "C"){
                rslt -= scores.top();
                scores.pop();
            } else{
                rslt += stoi(o);
                scores.push(stoi(o));
            }
        }

        return rslt;
    }
};