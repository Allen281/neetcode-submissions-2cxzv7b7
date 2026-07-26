class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int> prefixCount;
        prefixCount[0] = 1;
        int curSum = 0;
        int rslt = 0;

        for(int n : nums){
            curSum += n;

            rslt += prefixCount[curSum-k];
            prefixCount[curSum]++;
        }
        
        return rslt;
    }
};