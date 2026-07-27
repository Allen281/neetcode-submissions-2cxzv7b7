class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        vector<int> pSum(nums.size()+1);

        for(int i = 1; i <= nums.size(); i++){
            pSum[i] = pSum[i-1] + nums[i-1];
        }

        if(pSum[nums.size()] < target) return 0;

        int left = 0, right = nums.size();
        while(left+1 < right){
            int mid = (left+right)/2;

            bool canDo = false;
            for(int i = 0; i < pSum.size()-mid; i++){
                if(pSum[i+mid]-pSum[i] >= target){
                    canDo = true;
                    break;
                }
            }

            if(canDo) right = mid;
            else left = mid;
        }

        return right;
    }
};