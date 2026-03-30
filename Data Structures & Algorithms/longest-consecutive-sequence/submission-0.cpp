class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size() == 0) return 0;

        priority_queue<int> q;
        for(int n : nums) q.push(n);

        int rslt = 0;
        int counter = 1;
        int prev = q.top();
        q.pop();

        while(!q.empty()){
            if(q.top() == prev) q.pop();
            else if(q.top()+1 == prev){
                prev = q.top();
                q.pop();
                counter++;
            } else{
                prev = q.top();
                q.pop();
                rslt = max(rslt, counter);
                counter = 1;
            }
        }

        return max(rslt, counter);
    }
};
