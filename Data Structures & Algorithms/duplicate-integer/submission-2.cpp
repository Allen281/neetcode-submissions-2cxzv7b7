class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, bool> done;

        for(int n : nums){
            if(done[n]) return true;
            done[n] = true;
        }

        return false;
    }
};