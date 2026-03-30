class Solution {
public:
    vector<vector<int>> rslt;
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());

        dfs(candidates, -1, target, {});
        return rslt;
    }

    void dfs(vector<int>& candidates, int index, int target, vector<int> nums){
        if(target == 0){
            rslt.push_back(nums);
            return;
        } else if(target < 0) return;

        unordered_set<int> done;
        for(int i = index+1; i < candidates.size(); i++){
            if(candidates[i] > target) break;

            if(done.find(candidates[i]) != done.end()) continue;

            done.insert(candidates[i]);
            nums.push_back(candidates[i]);
            dfs(candidates, i, target-candidates[i], nums);
            nums.pop_back();
        }
    }
};
