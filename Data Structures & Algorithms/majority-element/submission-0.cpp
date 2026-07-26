class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> counts;

        for (int n : nums){
            counts[n] += 1;
            if (counts[n] > nums.size()/2) return n;
        }
    }
};