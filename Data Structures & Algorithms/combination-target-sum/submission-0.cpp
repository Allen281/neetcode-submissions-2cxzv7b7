class Solution {
public:
    vector<vector<int>> rslt;
    vector<int> cur;
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        dfs(nums, target, 0, 0);

        return rslt;    
    }

    void dfs(vector<int>& nums, int target, int index, int sum){
        if(sum == target){
            rslt.push_back(cur);
            return;
        } else if(sum > target){
            return;
        }

        for(int i = index; i < nums.size(); i++){
            cur.push_back(nums[i]);
            dfs(nums, target, i, sum+nums[i]);
            cur.erase(cur.end()-1);
        }
    }
};
