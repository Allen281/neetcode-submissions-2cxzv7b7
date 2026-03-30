class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> passedIndex;

        int left, right;
        for(int i = 0; i < nums.size(); i++){
            if(passedIndex.count(target-nums[i])){
                left = passedIndex[target-nums[i]];
                right = i;
                break;
            }

            passedIndex[nums[i]] = i; 
        }

        return {left, right};
    }
};
