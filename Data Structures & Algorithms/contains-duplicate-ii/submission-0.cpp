class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_set<int> window;

        int left = 0, right = 0;
        while(right < nums.size()){
            if(window.size() == k+1){
                window.erase(nums[left++]);
            }
            if(window.contains(nums[right])) return true;

            window.insert(nums[right++]);
        }

        return false;
    }
};