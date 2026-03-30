class Solution {
public:
    int findMin(vector<int> &nums) {
        int left = -1, right = nums.size();
        while(left+1 < right){
            int mid = (left+right)/2;

            if(nums[mid] > nums[nums.size()-1]) left = mid;
            else right = mid;
        }

        return nums[(left+1)%nums.size()];    
    }
};
